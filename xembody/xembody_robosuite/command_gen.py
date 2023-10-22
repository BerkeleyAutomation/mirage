# a script for generating commands 
# demo playback

# port = 10550
# horizon_dict = {"can": 400, "square": 400, "tool_hang": 700, "transport": 700}
# for task in ["can", "square"]:#, ["tool_hang", "transport"]:
#     for demo_type in ["ph", "mh"]:
#         if task == "tool_hang" and demo_type == "mh":
#             continue
#         # print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon {horizon_dict[task]} --seeds 0 --port {port} --demo_path /home/lawrence/xembody/robomimic/datasets/{task}/{demo_type}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/{task}/panda/{task}_{demo_type}_source_panda.txt")
#         # port += 1
#         for robot in ["Sawyer", "UR5e", "Kinova3", "Jaco", "IIWA"]:
        
#             # for tracking_error_threshold in [0.03]:
#             #     print("# source")
#             #     print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --demo_path /home/lawrence/xembody/robomimic/datasets/{task}/{demo_type}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/{task}/{robot.lower()}/{task}_{demo_type}_source_{robot.lower()}_1_delta.txt &")
#             #     print("# target")
#             #     print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --demo_path /home/lawrence/xembody/robomimic/datasets/{task}/{demo_type}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/{task}/{robot.lower()}/{task}_{demo_type}_target_{robot.lower()}_1_delta.txt --tracking_error_threshold {tracking_error_threshold} --num_iter_max 1 --robot_name {robot} --passive --delta_action")
#             #     print()
#             #     port += 1
                
                
#             # for tracking_error_threshold in [0.03]:
#             #     print("# source")
#             #     print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --demo_path /home/lawrence/xembody/robomimic/datasets/{task}/{demo_type}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/{task}/{robot.lower()}/{task}_{demo_type}_source_{robot.lower()}_1_absolute.txt &")
#             #     print("# target")
#             #     print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --demo_path /home/lawrence/xembody/robomimic/datasets/{task}/{demo_type}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/{task}/{robot.lower()}/{task}_{demo_type}_target_{robot.lower()}_1_absolute.txt --tracking_error_threshold {tracking_error_threshold} --num_iter_max 1 --robot_name {robot} --passive")
#             #     print()
#             #     port += 1
                
                
#             for tracking_error_threshold in [0.01]: #[0.04, 0.03, 0.02, 0.01]:
#                 print("# source")
#                 print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --demo_path /home/lawrence/xembody/robomimic/datasets/{task}/{demo_type}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/{task}/{robot.lower()}/{task}_{demo_type}_source_{robot.lower()}_{tracking_error_threshold}_300.txt &")
#                 print("# target")
#                 print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --demo_path /home/lawrence/xembody/robomimic/datasets/{task}/{demo_type}/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/{task}/{robot.lower()}/{task}_{demo_type}_target_{robot.lower()}_{tracking_error_threshold}_300.txt --tracking_error_threshold {tracking_error_threshold} --num_iter_max 300 --robot_name {robot} --passive")
#                 print()
#                 port += 1




# port = 20200
# horizon_dict = {"can": 400, "square": 400, "tool_hang": 700, "transport": 700}
# lowdim_dict = {"can": "can_ph_low_dim_epoch_1150_succ_100.pth", 
#                "square": "square_ph_low_dim_epoch_1850_succ_84.pth", 
#                "tool_hang": "tool_hang_ph_low_dim_epoch_2000_succ_14.pth", 
#                "transport": "transport_ph_low_dim_epoch_1000_succ_78.pth"}
# highdim_dict = {"can": "can_ph_image_epoch_300_succ_100.pth",
#                 "square": "square_ph_image_epoch_540_succ_78.pth",
#                 "tool_hang": "tool_hang_ph_image_epoch_440_succ_74.pth",
#                 "transport": "transport_ph_image_epoch_580_succ_70.pth"}

# for policy_type in ["lowdim", "highdim"]:
#     for task in ["can"]:# ["square"]:#, ["tool_hang", "transport"]:
#         if task in ["tool_hang", "transport"] and policy_type == "highdim":
#             continue
#         agent = lowdim_dict[task] if policy_type == "lowdim" else highdim_dict[task]
#         for robot in ["Sawyer", "UR5e", "Kinova3", "Jaco", "IIWA"]:
#             print("# source")
#             print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/passive_target/{robot.lower()}/{task}_{policy_type}_source_{robot.lower()}_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &")
#             print("# target")
#             print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/passive_target/{robot.lower()}/{task}_{policy_type}_target_{robot.lower()}_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name {robot} --passive --delta_action")
#             print()
#             port += 1
            
#             print()
#             print("# source")
#             print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/passive_target/{robot.lower()}/{task}_{policy_type}_source_{robot.lower()}_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &")
#             print("# target")
#             print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/passive_target/{robot.lower()}/{task}_{policy_type}_target_{robot.lower()}_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name {robot} --passive")
#             print()
#             port += 1
#             print()
            
#             for tracking_error_threshold in [0.04, 0.03, 0.02, 0.01]:
#                 print("# source")
#                 print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/passive_target/{robot.lower()}/{task}_{policy_type}_source_{robot.lower()}_{tracking_error_threshold}_300.txt &")
#                 print("# target")
#                 print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/passive_target/{robot.lower()}/{task}_{policy_type}_target_{robot.lower()}_{tracking_error_threshold}_300.txt --tracking_error_threshold {tracking_error_threshold} --num_iter_max 300 --robot_name {robot} --passive")
#                 print()
#                 port += 1
                

# # source
# python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# # target
# python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer                

port = 33100
horizon_dict = {"can": 400, "square": 400, "tool_hang": 700, "transport": 700}
lowdim_dict = {"can": "can_ph_low_dim_epoch_1150_succ_100.pth", 
               "square": "square_ph_low_dim_epoch_1850_succ_84.pth", 
               "tool_hang": "tool_hang_ph_low_dim_epoch_2000_succ_14.pth", 
               "transport": "transport_ph_low_dim_epoch_1000_succ_78.pth"}
highdim_dict = {"can": "can_ph_image_epoch_300_succ_100.pth",
                "square": "square_ph_image_epoch_540_succ_78.pth",
                "tool_hang": "tool_hang_ph_image_epoch_440_succ_74.pth",
                "transport": "transport_ph_image_epoch_580_succ_70.pth"}

for policy_type in ["lowdim", "highdim"]:
    for task in ["can", "square", "tool_hang", "transport"]:
        if task != "transport": continue
        if task in ["tool_hang", "transport"] and policy_type == "highdim":
            continue
        agent = lowdim_dict[task] if policy_type == "lowdim" else highdim_dict[task]
        for robot in ["Panda", "Sawyer", "UR5e", "Kinova3", "Jaco", "IIWA"]:
            if robot != "Jaco" and robot != "IIWA": continue
            print("# source")
            print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/active_target/{robot.lower()}/{task}_{policy_type}_source_{robot.lower()}_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &")
            print("# target")
            print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/active_target/{robot.lower()}/{task}_{policy_type}_target_{robot.lower()}_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name {robot} --delta_action")
            print()
            port += 1
            
            print()
            print("# source")
            print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/active_target/{robot.lower()}/{task}_{policy_type}_source_{robot.lower()}_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &")
            print("# target")
            print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/active_target/{robot.lower()}/{task}_{policy_type}_target_{robot.lower()}_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name {robot}")
            print()
            port += 1
            print()
            
            for tracking_error_threshold in [0.04, 0.03, 0.02, 0.01]:
                print("# source")
                print(f"python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/active_target/{robot.lower()}/{task}_{policy_type}_source_{robot.lower()}_{tracking_error_threshold}_300.txt --passive &")
                print("# target")
                print(f"python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon {horizon_dict[task]} --seeds 0 --connection --port {port} --agent /home/lawrence/xembody/robomimic/pretrained_models/{agent} --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/{task}/active_target/{robot.lower()}/{task}_{policy_type}_target_{robot.lower()}_{tracking_error_threshold}_300.txt --tracking_error_threshold {tracking_error_threshold} --num_iter_max 300 --robot_name {robot}")
                print()
                port += 1