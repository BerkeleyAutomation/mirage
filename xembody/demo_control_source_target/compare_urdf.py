
from tracikpy import TracIKSolver
import pybullet as p
import numpy as np
import robosuite.utils.transform_utils as T
ik_solver = TracIKSolver(
                "/home/lawrence/xembody/robosuite/robosuite/models/assets/bullet_data/panda_description/urdf/panda_arm.urdf",
                "panda_link0",
                "panda_link8",
            )

# ik_solver = TracIKSolver(
#                 "/home/lawrence/xembody/robosuite/robosuite/models/assets/bullet_data/panda_description/urdf/panda_arm_hand.urdf",
#                 "panda_link0",
#                 "panda_hand",
#             ) 

ik_solver = TracIKSolver(
                "/home/lawrence/Downloads/pybullet_ur5_robotiq/urdf/ur5_robotiq_85.urdf",
                "base_link",
                "robotiq_arg2f_base_link",
            )
# ee_out1 = ik_solver.fk([0,0,0,-0.0697999,0,0,0])
# ee_out1 = ik_solver.fk([1,1,1,-0.0697999,1,1,1])
ee_out1 = ik_solver.fk([0,0,0,0,0,0])
# print(T.mat2pose(ee_out1)[0] + np.array([-0.3090, 0, 0.82]))
print(ee_out1)

print()
# ik_solver = TracIKSolver(
#                 "/home/lawrence/Downloads/panda6/panda.urdf",
#                 "robot_base",
#                 "Cuboid",
#             )
ik_solver = TracIKSolver(
                "/home/lawrence/Downloads/ur5_no_reset_match/ur5.urdf",
                "robot_base",
                "UR5link7"
                # "ROBOTIQ85dummyMass",
            )
# ik_solver = TracIKSolver(
#                 "/home/lawrence/xembody/ur5e.urdf",
#                 "base_link",
#                 "ee_link",
#             )
# ee_out2 = ik_solver.fk([0,0,0,-0.0697999,0,0,0])
# ee_out2 = ik_solver.fk([1,1,1,-0.0697999,1,1,1])
# ee_out2 = ik_solver.fk([1,1,1, 1,1,1, 1])
# ee_out2 = ik_solver.fk([-2.71, -0.32, -2.24,  0.14, -0.96,  1.96 ])
ee_out2 = ik_solver.fk([0,0,0,0,0,0])
# ee_out2 = ik_solver.fk([ 2.8973,  1.,  2., -0.0697999, -2., -0.0175, 1.])

# ik_solver = TracIKSolver(
#                 "/home/lawrence/Downloads/ur5/ur5.urdf",
#                 "robot_base",
#                 "ROBOTIQ85dummyMass8",
#             )
# ee_out2 = ik_solver.fk([0,0,0,-0.0697999,0,0,0])
# ee_out2 = ik_solver.fk([1,1,1,-0.0697999,1,1,1])
# ee_out3 = ik_solver.fk([0,0,0,0,0,0, 1,1,1,-0.5])
# ee_out2 = (ee_out2 + ee_out3) / 2
print(ee_out2)
print(T.mat2pose(ee_out2))

# [0,0,0,-0.0697999,0,0,0]
# Pandalink1respondable
# ground truth ([-2.67871439e-01, -4.10348698e-02,  1.00747299e+00,  9.88845527e-01, -1.85744266e-03, -2.71851779e-04, -1.48933068e-01])
# predict [-0.267962, -0.006392,  1.083032]), array([-1.7320509e-07, -1.1920929e-07, -1.4297784e-07,  9.9999994e-01]

# Pandalink7respondable
# ground truth ([-0.16705622, -0.01822134,  1.70278275, -0.65305269,  0.27064443, 0.65357542,  0.27039424])
# predict [-0.15280786, -0.00617225,  1.78123945]), array([ 9.9939108e-01,  8.0093741e-07, -3.4891851e-02,  3.1735115e-07]

# Pandagripper
# ground truth ([-1.79185912e-01, -6.18561590e-03,  1.65729642e+00,  9.23878491e-01, 3.82685900e-01, -2.92408251e-04, -9.49430687e-05])
# predict [-0.16027017, -0.00617232,  1.67449998]), array([ 0.7066764 , -0.7066759 , -0.02467191,  0.02467214]

# Cuboid (Panda_tip)
# ground truth ([-1.77836508e-01, -7.60168768e-03,  1.56524849e+00, -3.82671773e-01, 9.23884332e-01,  1.03227139e-04, -3.53276555e-04])
# predict [-0.16653252, -0.00759036,  1.56473446]), array([ 0.38245085, -0.9233169 , -0.01335165,  0.03223627]

# [1,1,1,-0.0697999,1,1,1]
# Cuboid (Panda_tip)
# ground truth ([-0.17441767,  0.52914542,  1.51605844, -0.62678498,  0.32519913, 0.58129519, -0.40432918])
# predict [-0.18880384,  0.54286782,  1.50361912]), array([ 0.62642395, -0.3249898 , -0.5611975 ,  0.4324723 ]

# [ 2.8973,  1.,  2., -0.0697999, -2., -0.0175, 1.]
# Cuboid (Panda_tip)
# ground truth [-0.7039116 ,  0.10384046,  1.27257013, -0.85043889,  0.19855784, -0.4871127 , -0.00705621]
# predict [-0.71055583,  0.09458275,  1.28120632]), array([-0.8602388 ,  0.18554759, -0.4744714 ,  0.02093422]

# ee_out = (ee_out1 + ee_out2) / 2
# print("Predict:", ee_out)
# print(T.mat2pose(ee_out))


#ur5 UR5_tip [0,0,0,0,0,0]
# ground truth ([-6.34098649e-01, -1.45757571e-04,  1.80647635e+00,  6.36964542e-05, -7.07227111e-01, -1.31065084e-04,  7.06986487e-01])
# predict ROBOTIQ85dummyMass: [-1.47890326e+00, -1.06904045e-04,  1.75664743e+00]), array([ 1.0860413e-07, -7.0710719e-01, -5.9519402e-07,  7.0710629e-01]
# ROBOTIQ85dummyMass7, ROBOTIQ85dummyMass8, [0,0,0, (0)][-5.53903245e-01, -1.07474635e-04,  1.73146227e+00]), array([ 0.28867492, -0.28867614,  0.28867418,  0.86602545]
# ROBOTIQ85dummyMass7, ROBOTIQ85dummyMass8, [1,1,1, (1)] [-6.90673858e-02, -1.08483110e-04,  2.07862167e+00]), array([0.39173472, 0.16185737, 0.11493737, 0.89840704]

#ur5 UR5_tip [1,1,1,1,1,1,1]
# ground truth ([-1.19429028,  0.29961726,  0.8929528 , -0.59490633,  0.2941716 , 0.66904533, -0.3345564 ])
# predict ROBOTIQ85dummyMass: [-2.03261588,  0.29543274,  0.9518963 ]), array([ 0.59500974, -0.29426026, -0.6688838 ,  0.33461726]

# robot_urdf = "/home/lawrence/xembody/robosuite/robosuite/models/assets/bullet_data/panda_description/urdf/panda_arm.urdf"
# ik_robot = p.loadURDF(fileName=robot_urdf, useFixedBase=1, physicsClientId=0)

# bullet_ee_idx = p.getNumJoints(ik_robot, physicsClientId=0) - 1
# eef_pos_in_world = np.array(
#             p.getLinkState(ik_robot, bullet_ee_idx, physicsClientId=0)[0]
#         )
# eef_orn_in_world = np.array(
#             p.getLinkState(ik_robot, bullet_ee_idx, physicsClientId=0)[1]
#         )
# eef_pose_in_world = T.pose2mat((eef_pos_in_world, eef_orn_in_world))



# ik_solution = list(
#             p.calculateInverseKinematics(
#                 bodyUniqueId=,
#                 endEffectorLinkIndex=self.bullet_ee_idx,
#                 targetPosition=target_position,
#                 targetOrientation=target_orientation,
#                 lowerLimits=list(self.sim.model.jnt_range[self.joint_index, 0]),
#                 upperLimits=list(self.sim.model.jnt_range[self.joint_index, 1]),
#                 jointRanges=list(
#                     self.sim.model.jnt_range[self.joint_index, 1] - self.sim.model.jnt_range[self.joint_index, 0]
#                 ),
#                 restPoses=self.rest_poses,
#                 jointDamping=[0.1] * self.num_bullet_joints,
#                 physicsClientId=self.bullet_server_id,
#             )
#         )
# list(np.array(ik_solution)[self.ik_command_indexes])