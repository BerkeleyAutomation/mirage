import numpy as np
from tracikpy import TracIKSolver

ur5_solver = TracIKSolver("/home/lawrence/cross_embodiment_ws/src/gazebo_env/description/urdf/ur5_ik_real.urdf","base_link","wrist_3_link")
panda_solver = TracIKSolver("/home/lawrence/cross_embodiment_ws/src/gazebo_env/description/urdf/panda_ur5_gripper_ik_real.urdf","panda_link0","panda_link8")
ee_pose = panda_solver.fk(np.array([0.05445501208305359, 0.29904165863990784, -0.05337003618478775, -2.1572153568267822, 0.010299555025994778, 2.438530683517456,0.003930782433599234]))
print(ee_pose)
qout = panda_solver.ik(ee_pose,qinit=np.zeros(panda_solver.number_of_joints))
print(qout)
# panda_fk_solver = TracIKSolver("/home/benchturtle/cross_embodiment_ws/src/gazebo_env/description/urdf/panda_arm_hand_only_ik.urdf","world","panda_hand")
# ee_pose = panda_fk_solver.fk(np.zeros(panda_fk_solver.number_of_joints))
# ur5e_ik_solver = TracIKSolver("/home/benchturtle/cross_embodiment_ws/src/gazebo_env/description/urdf/ur5e_nvidia_with_gripper_solo_ik.urdf","world","tool0")
# qout = ur5e_ik_solver.ik(ee_pose,qinit=np.zeros(ur5e_ik_solver.number_of_joints))
# print(qout)

#print(ur5e_ik_solver.fk(np.array([0,0,0,0,0,0])))