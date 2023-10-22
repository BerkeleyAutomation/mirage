# a script for generating commands 
# example
"""# source
    python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift_lowdim_source_panda_0.015_300.txt 
    # target
    python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift_lowdim_target_panda_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Panda --passive """
    
# port = 50000
# for robot in ["Sawyer", "UR5e", "Kinova3", "Jaco", "IIWA"]:
#     if robot == "IIWA":
#         for demo_type in ["ph", "mh"]:
#             print("#############################################################################################################################")
#             print("#############################################################################################################################")
#             for tracking_error_threshold in [0.04, 0.03, 0.02, 0.015, 0.007, 0.003, 0.001]:
#                 print("# source")
#                 print("python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port {} --demo_path /home/lawrence/xembody/robomimic/datasets/lift/{}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/{}/lift_{}_source_{}_{}_300.txt &".format(port, demo_type, robot.lower(), demo_type, robot.lower(), tracking_error_threshold))
#                 print("# target")
#                 print("python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port {} --demo_path /home/lawrence/xembody/robomimic/datasets/lift/{}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/{}/lift_{}_target_{}_{}_300.txt --tracking_error_threshold {} --num_iter_max 300 --robot_name {} --passive".format(port, demo_type, robot.lower(), demo_type, robot, tracking_error_threshold, tracking_error_threshold, robot))
#                 print()
#                 port += 1
                
                
port = 61000
for robot in ["Sawyer", "UR5e", "Kinova3", "Jaco", "IIWA"]:
    for demo_type in ["ph", "mh"]:
        for tracking_error_threshold in [0.03]:
            print("# source")
            print("python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port {} --demo_path /home/lawrence/xembody/robomimic/datasets/lift/{}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/{}/lift_{}_source_{}_1_delta.txt &".format(port, demo_type, robot.lower(), demo_type, robot.lower()))
            print("# target")
            print("python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port {} --demo_path /home/lawrence/xembody/robomimic/datasets/lift/{}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/{}/lift_{}_target_{}_1_delta.txt --tracking_error_threshold {} --num_iter_max 1 --robot_name {} --passive --delta_action".format(port, demo_type, robot.lower(), demo_type, robot.lower(), tracking_error_threshold, robot))
            print()
            port += 1