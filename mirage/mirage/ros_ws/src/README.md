# Cross Embodiment

Hi. Welcome to this test workspace for the cross embodiment project. This is currently in development.

## Installation
When doing this installation, have conda fully deactivated
Make sure ROS2 Humble Desktop Full is installed: https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

Also, setup ros2 control: https://control.ros.org/humble/doc/ros2_control_demos/doc/index.html.
Note, when doing the rosdep install, make sure you don't do sudo if you do normal rosdep update without sudo.

Create Mamba Environment

Mamba setup from this link: https://robofoundry.medium.com/using-robostack-for-ros2-9bb52ca89c12

curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"

bash Mambaforge-$(uname)-$(uname -m).sh

source ~/.bashrc

conda install mamba -c conda-forge

mamba create -n gazebo_ros_env python=3.10.12

mamba activate gazebo_ros_env

Mix of this link: https://robofoundry.medium.com/using-robostack-for-ros2-9bb52ca89c12

And then this link: https://robostack.github.io/GettingStarted.html

conda config --env --add channels conda-forge

conda config --env --add channels robostack

conda config --env --add channels robostack-humble

conda config --env --add channels robostack-experimental

mamba install ros-humble-desktop-full # Will fail

conda config --env --add channels conda-forge

conda config --env --add channels robostack-staging

conda config --env --remove channels defaults

mamba install ros-humble-desktop

mamba install ros-humble-desktop-full

Tracikpy Installation Link: https://github.com/mjd3/tracikpy

sudo apt-get install libeigen3-dev liborocos-kdl-dev libkdl-parser-dev liburdfdom-dev libnlopt-dev

cd ~/

git clone https://github.com/mjd3/tracikpy.git

pip install tracikpy/

pip install kinpy

To make it so the plugins work for Gazebo, add this to the bashrc:
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/cross_embodiment_ws/build/gazebo_env
## Repo Setup
```
mkdir -p ~/cross_embodiment_test_ws/src
cd ~/cross_embodiment_test_ws
git clone <LINK> src
colcon build
. install/setup.bash
```

## Fk_Ik_Rviz_Pkg
This package has python scripts to analyze URDFs to provide forward and inverse kinematics.

## Gazebo_Env
This package will launch a UR5E robot in Gazebo. It has simulated hardware control so you can move the robot to the desired position. A sample script is also provided to move the robot to some preplanned positions.

Need to import kinpy
