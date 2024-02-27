#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from message_filters import Subscriber, TimeSynchronizer
import cv2
from cv_bridge import CvBridge
import numpy as np
from scipy.ndimage import generic_filter

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.cv_bridge_ = CvBridge()
        depth_image_sub = Subscriber(self, Image, '/ur5_camera/image_raw')
        depth_depth_image_sub = Subscriber(self, Image, '/ur5_camera/depth/image_raw')

        # Synchronize the two image topics based on their timestamps
        ts = TimeSynchronizer([depth_image_sub, depth_depth_image_sub], 10)
        ts.registerCallback(self.callback)

    def normalize_depth_image(self,depth_image):
        # Define the minimum and maximum depth values in your depth image
        min_depth = np.min(depth_image)
        max_depth = np.max(depth_image)

        # Normalize the depth image to the range [0, 1]
        normalized_depth_image = (depth_image - min_depth) / (max_depth - min_depth)

        # Optionally, you can scale the normalized image to a different range
        # For example, to scale it to [0, 255] for visualization:
        normalized_depth_image = (normalized_depth_image * 255).astype(np.uint8)
        return normalized_depth_image
    
    def replace_inf_with_neighbors_average(self,array):
        def replace_function(subarray):
            center = subarray[4]
            if(center != np.inf and center != -np.inf and center != np.nan):
                return center
            valid_values = subarray[subarray != -np.inf]
            if valid_values.size == 0:
                return np.nan
            else:
                return np.nanmean(valid_values)

        return generic_filter(array, replace_function, size=(3, 3), mode='constant', cval=np.nan)


    def inpainting(self,rgb,depth,seg_file,gazebo_rgb,gazebo_seg,gazebo_depth):
        # TODO(kush): Clean this up to use actual data, not file names
        if type(rgb) == str:
            rgb_np = cv2.imread(rgb)
            seg = cv2.imread(seg_file,0)
            depth_np = np.load(depth)
            return
        else:
            rgb_np = np.array(rgb,dtype=np.uint8)
            depth_np = np.array(depth,dtype=np.float64)
            seg = seg_file

        _, seg = cv2.threshold(seg, 128, 255, cv2.THRESH_BINARY)
        robosuite_depth_image_unmasked = depth_np
        robosuite_rgb_image_unmasked = rgb_np
        robosuite_segmentation_mask_255 = seg
        gazebo_robot_only_rgb = gazebo_rgb
        gazebo_segmentation_mask_255 = gazebo_seg
        gazebo_robot_only_depth = gazebo_depth
        robosuite_rgbd_image_unmasked = np.concatenate((robosuite_rgb_image_unmasked,robosuite_depth_image_unmasked[:,:,np.newaxis]),axis=2)
        inverted_robosuite_segmentation_mask_255 = cv2.bitwise_not(robosuite_segmentation_mask_255)
        robosuite_rgbd_image_masked = cv2.bitwise_and(robosuite_rgbd_image_unmasked,robosuite_rgbd_image_unmasked,mask=inverted_robosuite_segmentation_mask_255)
        robosuite_rgb_image_masked = robosuite_rgbd_image_masked[:,:,0:3].astype(np.uint8)
        robosuite_depth_image_masked = robosuite_rgbd_image_masked[:,:,-1]
        joined_depth = np.concatenate((gazebo_robot_only_depth[np.newaxis],robosuite_depth_image_masked[np.newaxis]),axis=0)
        joined_depth[0,:,:][joined_depth[0,:,:] == 0] = 1000
        joined_depth[1,:,:][joined_depth[1,:,:] == 0] = 5
        joined_depth_argmin = np.argmin(joined_depth,axis=0)
        
        robosuite_rgb_image_masked_inpaint = cv2.inpaint(robosuite_rgb_image_masked,robosuite_segmentation_mask_255,inpaintRadius=3,flags=cv2.INPAINT_TELEA)
        attempt = robosuite_rgb_image_masked_inpaint * joined_depth_argmin[:,:,np.newaxis]
        inverted_joined_depth_argmin = 1 - joined_depth_argmin
        gazebo_robot_only_lab = cv2.cvtColor(gazebo_robot_only_rgb,cv2.COLOR_BGR2LAB)
        gazebo_robot_only_lab[:,:,0] += 50
        gazebo_robot_only_mod = cv2.cvtColor(gazebo_robot_only_lab,cv2.COLOR_LAB2BGR)
        gazebo_robot_only_rgb = gazebo_robot_only_mod
        attempt2 = gazebo_robot_only_rgb * inverted_joined_depth_argmin[:,:,np.newaxis]
        inpainted_image = attempt + attempt2
        image_8bit = cv2.convertScaleAbs(inpainted_image)  # Convert to 8-bit image
        cv2.imwrite('gazebo_inpaint.png',image_8bit)

    def dummyInpainting(self,rgb,gazebo_rgb,gazebo_seg):
        import pdb
        pdb.set_trace()
        _, gazebo_seg = cv2.threshold(gazebo_seg, 128, 255, cv2.THRESH_BINARY)
        gazebo_segmentation_mask_255 = gazebo_seg
        inverted_segmentation_mask_255_original = cv2.bitwise_not(gazebo_seg)
        cv2.imwrite('inverted_mask1.png',inverted_segmentation_mask_255_original)
        inverted_segmentation_mask_255 = cv2.erode(inverted_segmentation_mask_255_original,np.ones((3,3),np.uint8),iterations=10)
        cv2.imwrite('inverted_mask2.png',inverted_segmentation_mask_255)
        outline_mask = abs(inverted_segmentation_mask_255 - inverted_segmentation_mask_255_original)*255
        gazebo_only = cv2.bitwise_and(gazebo_rgb,gazebo_rgb,mask=gazebo_segmentation_mask_255)
        gazebo_only = cv2.cvtColor(gazebo_only,cv2.COLOR_BGR2RGB)
        cv2.imwrite('gazebo_robot_only.png',gazebo_only)
        background_only = cv2.bitwise_and(rgb,rgb,mask=inverted_segmentation_mask_255)
        cv2.imwrite('background_only.png',background_only)
        background_only_filled = cv2.inpaint(background_only,outline_mask,3,cv2.INPAINT_TELEA)
        cv2.imwrite('background_only_filled.png',background_only_filled)
        dummy_inpaint = gazebo_only + background_only_filled
        cv2.imwrite('dummy_inpaint.png',dummy_inpaint)
        ultimate_robot = cv2.imread('/home/benchturtle/cross_embodiment_ws/ultimate_robot.png')
        ultimate_background = cv2.imread('/home/benchturtle/cross_embodiment_ws/ultimate_background.png')
        cv2.imwrite('smart_inpaint.png',ultimate_robot+ultimate_background)

    def callback(self, rgb_image_msg, depth_image_msg):
        gazebo_rgb_np = self.cv_bridge_.imgmsg_to_cv2(rgb_image_msg)
        
        cv2.imwrite('gazebo_rgb.png',gazebo_rgb_np)
        gazebo_depth_np = self.cv_bridge_.imgmsg_to_cv2(depth_image_msg)
        cv2.imwrite('inf_mask.png',(np.isinf(gazebo_depth_np)*255).astype(np.uint8))
        normalized_depth_image = self.normalize_depth_image(gazebo_depth_np)
        cv2.imwrite('gazebo_norm_depth.png',normalized_depth_image)
        gazebo_seg_np = (gazebo_depth_np < 8).astype(np.uint8)
        gazebo_seg_255_np = 255 * gazebo_seg_np
        cv2.imwrite('gazebo_seg.png',gazebo_seg_255_np)
        robosuite_rgb = cv2.imread('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/real_check/ur5e_check_0.png')
        
        robosuite_depth = np.load('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/real_check/ur5e_depth_0.npy')
        cv2.imwrite('real_rgb.png',robosuite_rgb)
        cv2.imwrite('nan_depth_mask.png',(np.isnan(robosuite_depth)*255).astype(np.uint8))
        cv2.imwrite('inf_depth_mask.png',(np.isinf(robosuite_depth)*255).astype(np.uint8))
        inf_mask = (np.isinf(robosuite_depth)*255).astype(np.uint8)
        robosuite_depth_inf_filled = cv2.inpaint(robosuite_depth,inf_mask,1,cv2.INPAINT_TELEA)
        cv2.imwrite('inf_depth_mask2.png',(np.isinf(robosuite_depth_inf_filled)*255).astype(np.uint8))
        nan_mask = (np.isnan(robosuite_depth_inf_filled)*255).astype(np.uint8)
        robosuite_depth_inf_filled_nan_filled = cv2.inpaint(robosuite_depth_inf_filled,nan_mask,1,cv2.INPAINT_TELEA)
        cv2.imwrite('nan_depth_mask2.png',(np.isnan(robosuite_depth_inf_filled_nan_filled)*255).astype(np.uint8))
        robosuite_depth_no_nan = np.nan_to_num(robosuite_depth_inf_filled_nan_filled, nan=0)
        normalized_robosuite_depth_image = self.normalize_depth_image(robosuite_depth_no_nan)
        cv2.imwrite('real_depth.png',normalized_robosuite_depth_image)
        robosuite_depth = gazebo_depth_np
        robosuite_seg = gazebo_seg_255_np
        self.dummyInpainting(robosuite_rgb,gazebo_rgb_np,gazebo_seg_255_np)
        # Depth image callback logic
        self.get_logger().info('Received synchronized depth camera images')

def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    rclpy.spin(image_subscriber)

    image_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
