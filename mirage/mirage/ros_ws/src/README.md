# Mirage

Hi! Welcome to the ROS workspace setup for Mirage. This README details how to setup the ROS2 environment and Gazebo to run simulated and real experiments in the Mirage paper.

## Prerequisites
Computer with Ubuntu 22.04

## Installation (Bash Script)
Clone the repo: 
```
cd ~/
git clone --recurse-submodules git@github.com:BerkeleyAutomation/mirage.git
```

Run the setup bash script
```
cd ~/mirage/xembody/xembody/src/ros_ws/src
bash ros_gazebo_setup.bash
```

## Installation (Step by Step)

### Step 1: Install ROS2 Humble Full: https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
```
# Step 1.1 Set Locale
sudo apt update -y
sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# Step 1.2 Setup Sources
sudo apt install software-properties-common
echo -ne '\n' | sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Step 1.3 Install ROS2 Packages
sudo apt update -y
sudo apt upgrade -y
sudo apt install ros-humble-desktop-full -y
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

### Step 2: Setup ROS2 Control: https://control.ros.org/humble/doc/ros2_control_demos/doc/index.html
```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/ros-controls/ros2_control_demos -b humble
cd ~/ros2_ws/
sudo apt-get update
sudo rosdep install --from-paths ./ -i -y --rosdistro ${ROS_DISTRO}
cd ~/ros2_ws/
. /opt/ros/${ROS_DISTRO}/setup.sh
colcon build --merge-install
```

### Step 3: Tracikpy Installation: https://github.com/mjd3/tracikpy
```
sudo apt-get install libeigen3-dev liborocos-kdl-dev libkdl-parser-dev liburdfdom-dev libnlopt-dev
cd ~/
git clone https://github.com/mjd3/tracikpy.git
pip install tracikpy/
```

### Step 4: Make sure Gazebo plugins can be found: https://classic.gazebosim.org/tutorials?tut=guided_i5
```
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/mirage/xembody/xembody/src/ros_ws/build/gazebo_env" >> ~/.bashrc
```

### Step 5: Compile workspace
```
cd ~/mirage/xembody/xembody/src/ros_ws
colcon build
. install/setup.bash
source ~/.bashrc
```
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
