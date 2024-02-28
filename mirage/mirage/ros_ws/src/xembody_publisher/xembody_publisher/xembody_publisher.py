from mirage.infra.ros_inpaint_publisher_sim import ROSInpaintPublisherSim
import numpy as np
import threading
import os
import time
import rclpy
import pickle

def start_publisher(data_file_path):
    ros_inpaint_publisher = ROSInpaintPublisherSim()
    spin_thread = threading.Thread(target=rclpy.spin, args=(ros_inpaint_publisher.node,)).start()
    
    data_file_path = os.path.join(data_file_path, 'data.pkl')
    data_result_file_path = os.path.join(data_file_path, 'return_data.pkl')
    while True:
        if os.path.exists(data_file_path):
            with open(data_file_path, 'rb') as f:
                data = pickle.load(f)
            import pdb; pdb.set_trace()
            rgb_image = data['rgb_image']
            point_cloud = data['point_cloud']
            segmentation_mask = data['segmentation_mask']
            joint_angles = data['joint_angles']
            ros_inpaint_publisher.publish_to_ros_node(rgb_image, point_cloud, segmentation_mask, joint_angles)
            os.remove(data_file_path)
            
            # Now, wait for the result and write it to a data file
            inpainted_image = ros_inpaint_publisher.get_inpainted_image(True)
            np.save(data_result_file_path, {'inpainted_image': inpainted_image})
            
        time.sleep(0.01)
    
    spin_thread.join()
    
def main():
    data_file_path = os.path.join('/home/lawrence/xembody/xembody/xembody/src/orbit/data_exchange_dir')
    start_publisher(data_file_path)

if __name__ == '__main__':
    main()