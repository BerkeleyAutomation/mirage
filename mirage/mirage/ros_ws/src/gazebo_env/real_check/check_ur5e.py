import numpy as np
import cv2
check_panda_np = np.load('check_ur5.npy',allow_pickle=True)
check_panda_dict = check_panda_np.tolist()
cam_extrinsic_matrix = check_panda_dict['cam_extrinsic_matrix']
cam_intrinsic_matrix = check_panda_dict['cam_intrinsic_matrix']
img0 = check_panda_dict['img_0']
img1 = check_panda_dict['img_1']
img2 = check_panda_dict['img_2']
img3 = check_panda_dict['img_3']
img4 = check_panda_dict['img_4']
imgs = [img0,img1,img2,img3,img4]
for i in range(len(imgs)):
    img_data = imgs[i]
    rgb = img_data['img']
    depth = img_data['depth']
    joint_angles = img_data['joint_angles']
    ee_pose = img_data['ee_pose']
    cv2.imwrite('ur5e_check_'+str(i)+'.png',rgb)
    np.save('ur5e_depth_'+str(i)+'.npy',depth)
    print("IMG " + str(i))
    print("Joint angles: " + str(joint_angles))
    print("EE Pose: " + str(ee_pose))
    print("\n")