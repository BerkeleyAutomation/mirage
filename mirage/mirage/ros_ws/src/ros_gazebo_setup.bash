#!/bin/bash
# Step 1: Install ROS2 Humble Full: https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

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

# Step 2: Setup ROS2 Control: https://control.ros.org/humble/doc/ros2_control_demos/doc/index.html
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/ros-controls/ros2_control_demos -b humble
cd ~/ros2_ws/
sudo apt-get update
sudo rosdep install --from-paths ./ -i -y --rosdistro ${ROS_DISTRO}
cd ~/ros2_ws/
. /opt/ros/${ROS_DISTRO}/setup.sh
colcon build --merge-install

# Step 3: Tracikpy Installation: https://github.com/mjd3/tracikpy
sudo apt-get install libeigen3-dev liborocos-kdl-dev libkdl-parser-dev liburdfdom-dev libnlopt-dev
cd ~/
git clone https://github.com/mjd3/tracikpy.git
pip install tracikpy/

# Step 4: Make sure Gazebo plugins can be found: https://classic.gazebosim.org/tutorials?tut=guided_i5
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/mirage/xembody/xembody/src/ros_ws/build/gazebo_env" >> ~/.bashrc

# Step 5: Compile workspace
cd ~/mirage/xembody/xembody/src/ros_ws
colcon build
. install/setup.bash
source ~/.bashrc