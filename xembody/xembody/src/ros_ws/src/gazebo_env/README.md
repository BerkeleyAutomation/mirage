# Gazebo_Env
This package will launch a UR5E robot in Gazebo. It has simulated hardware control so you can move the robot to the desired position.

## Installation
First, make sure you have [ROS2 Humble installed on Ubuntu 22.04](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
Next, you need to have some stuff installed for ros2 control. I personally had trouble setting it up the normal way, so I actually made a separate workspace, and installed it with the ros2 control demos. Since the installation is systemwide, it will properly install everything so this repo can work. You can find the link [here](https://control.ros.org/master/doc/ros2_control_demos/doc/index.html#build-from-debian-packages) to build from debian packages.

## Launching
Before launching, there are 2 things you need to make sure you do.

1. In the URDF, there is a hardcoded file path to the urbot_controllers.yaml. I couldn't figure out a relative path way to do that, so you will have to manually edit it.
2. You need to make sure the No Physics plugin can be found by the launch file, so add this line to your ~/.bashrc.

```export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:~/cross_embodiment_test_ws/build/gazebo_env```

To launch a Gazebo simulation of the UR5e, run the following:

```
cd ~/cross_embodiment_test_ws
colcon build
. install/setup.bash
ros2 launch gazebo_env ur5e_gazebo_classic.launch.py
```

This should launch a Gazebo environment with the UR5E loaded in it. To move it based on joint angles, open a new terminal and type this:
```
ros2 topic pub /forward_position_controller/commands std_msgs/msg/Float64MultiArray "data:
- 0.5
- -0.5
- 1.0
- 0
- 0
- 0"
```

It should snap to the right position immediately, and not jitter.

If you want to see the robot move to some different positions (indicated by red and green cubes, run the following:
```
cd ~/cross_embodiment_test_ws
colcon build
. install/setup.bash
ros2 launch gazebo_env ur5e_gazebo_classic.launch.py
```
TODO: Add the thing about LD_LIBRARY_PATH, also changing the hardcoded parameters, also ros2 control installation