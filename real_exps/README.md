# Mirage Real Experiments
To evaluate a trajectory with inpainting on a real robot, first start the ROS / Gazebo Inpainting environment.
In terminal 1:
```
source mirage/mirage/ros_ws/install/setup.bash
ros2 launch gazebo_env {real_launch_file}.launch.py
```
`real_launch_file` can be any of the launch files that is not the robosuite. Different launch files correspond to different parts of the robot being inpainted or not being inpainted. 

In terminal 2:
```
source mirage/mirage/ros_ws/install/setup.bash
ros2 run gazebo_env {real_launch_file}.py
```
For the corresponding writer node, it should have the same suffix as the corresponding launch file.

Then, fill in the appropriate the appropriate path to the real life model in `model_config_mapping` in `evaluate_robomimic.py`.
In terminal 3, run:
```
python3 evaluate_robomimic.py
```

Note: The robot_env_xembody.py encapsulate a real robot in a typical gym environment.