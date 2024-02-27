#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from input_filenames_msg.msg import InputFilesRealData
import numpy as np
import cv2
from cv_bridge import CvBridge
import open3d as o3d
import time
class ReprojectTestNode(Node):
    def __init__(self):
        super().__init__('reproject_test_node')
        self.cv_bridge_ = CvBridge()
        self.intrinsic_matrix_ = np.array([[524.22595215,   0.        , 639.77819824],
                                           [  0.        , 524.22595215, 370.27804565],
                                           [0,0,1]])
        self.subscription_data_ = self.create_subscription(
            InputFilesRealData,
            'input_files_data_real',
            self.listenerCallbackOnlineDebug,
            1)
        
        
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
    
    def listenerCallbackOnlineDebug(self,msg):
        start_time = time.time()
        rgb_np = self.cv_bridge_.imgmsg_to_cv2(msg.rgb)
        depth_np = np.array(msg.depth_map,dtype=np.float64).reshape((msg.rgb.height,msg.rgb.width))
        depth_np[np.isinf(depth_np) & (depth_np < 0)] = 0.01
        depth_np[np.isinf(depth_np) & (depth_np > 0)] = 10
        depth_np[np.isnan(depth_np)] = 0.0001
        cv2.imwrite('reproject_og_depth.png',self.normalize_depth_image(depth_np))
        cv2.imwrite('reproject_rgb.png',rgb_np)
        fx = self.intrinsic_matrix_[0][0]
        fy = self.intrinsic_matrix_[1][1]
        cx = self.intrinsic_matrix_[0][2]
        cy = self.intrinsic_matrix_[1][2]
        u = np.tile(np.arange(rgb_np.shape[1]), (rgb_np.shape[0], 1))
        v = np.tile(np.arange(rgb_np.shape[0]),(rgb_np.shape[1],1)).T
        d = depth_np
        z = d
        x = (u - cx) * z / fx
        y = (v - cy) * z / fy
        xyz_np = np.stack([x,y,z],axis=-1)
        keys = xyz_np.reshape(-1,3)
        values = rgb_np.reshape(-1,3)
        data_dict = dict(zip(map(tuple,keys),map(tuple,values)))
        points = np.array([x.reshape(-1),y.reshape(-1),z.reshape(-1)]).T
        
        new_frame_to_old_frame = np.array([[0.98,0,0.199,0],
                                           [0,1,0,0],
                                           [-0.199,0,0.980,0],
                                           [0,0,0,1]])
        homogenous_points = np.column_stack((points, np.ones(len(points))))
        # Create an Open3D point cloud
        #point_cloud = o3d.geometry.PointCloud()
        #point_cloud.points = o3d.utility.Vector3dVector(points)
        #coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1, origin=[0, 0, 0])

        # Visualize the point cloud
        #o3d.visualization.draw_geometries([point_cloud,coordinate_frame])
        transformed_points = np.dot(new_frame_to_old_frame, homogenous_points.T).T[:, :3]
        point_dict = dict(zip(map(tuple,transformed_points),map(tuple,homogenous_points)))
        new_image_mask = np.zeros((msg.rgb.height,msg.rgb.width)).astype(np.uint8)
        new_image = np.zeros((msg.rgb.height,msg.rgb.width,3)).astype(np.uint8)
        new_fx = fx
        new_fy = fy
        new_cx = cx
        new_cy = cy
        # Vectorized computation of coordinates
        u_coords = np.round((new_fx * transformed_points[:, 0] / transformed_points[:, 2]) + new_cx).astype(int)
        v_coords = np.round((new_fy * transformed_points[:, 1] / transformed_points[:, 2]) + new_cy).astype(int)

        valid_coords_mask = np.logical_and.reduce([
            (0 <= u_coords), (u_coords < msg.rgb.width),
            (0 <= v_coords), (v_coords < msg.rgb.height),
            ~np.isnan(transformed_points).any(axis=1)
        ])

        # Convert lists to tuples before using them as keys
        point_keys = tuple(map(tuple, transformed_points[valid_coords_mask].tolist()))
        data_values = np.array([data_dict[point_dict[key][:3]] for key in point_keys], dtype=np.uint8)
        new_image_mask[v_coords[valid_coords_mask], u_coords[valid_coords_mask]] = 255
        new_image[v_coords[valid_coords_mask], u_coords[valid_coords_mask]] = data_values

        #new_image_mask[v_coords[valid_coords_mask], u_coords[valid_coords_mask]] = 255
        #new_image[v_coords[valid_coords_mask], u_coords[valid_coords_mask]] = data_dict[
        #    tuple(transformed_points[valid_coords_mask].astype(int).tolist())[:3]]
        
        inverted_image_mask = cv2.bitwise_not(new_image_mask)
        print("Time before inpaint: " ,time.time()-start_time)
        inpainted_image = cv2.inpaint(new_image,inverted_image_mask,1,cv2.INPAINT_TELEA)
        print('Time taken for reprojecting: ',time.time()-start_time)
        
        cv2.imwrite('image_overlap.png',new_image_mask)
        cv2.imwrite('image_overlap_color.png',new_image)
        cv2.imwrite('image_overlap_inpaint.png',inpainted_image)
        

        
        

def main(args=None):
    rclpy.init(args=args)

    write_data = ReprojectTestNode()

    rclpy.spin(write_data)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    write_data.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()