# Copyright 2021 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Declare arguments
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "gui",
            default_value="false",
            description="Start RViz2 automatically with this launch file.",
        )
    )

    # Initialize Arguments
    gui = LaunchConfiguration("gui")

    gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [PathJoinSubstitution([FindPackageShare("gazebo_ros"), "launch", "gzserver.launch.py"])]
        )
    )
    gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [PathJoinSubstitution([FindPackageShare("gazebo_ros"), "launch", "gzclient.launch.py"])]
        )
    )

    # Get URDF via xacro
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
               [FindPackageShare("gazebo_env"), "urdf", "ur5_with_gripper_camera_scene_real.urdf.xacro"]
            ),
            " ",
            "use_gazebo_classic:=true",
            # PathJoinSubstitution([FindExecutable(name="xacro")]),
            # " ",
            # PathJoinSubstitution(
            #     [FindPackageShare("gazebo_env"), "urdf", "d435.urdf"]
            # ),
        ]
    )
    robot_description = {"robot_description": robot_description_content}

    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "urbot_system_position"],
        output="screen",
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    joint_state_publisher_node = Node(
        package="gazebo_env",
        executable="full_ur5e_joint_state_publisher_node.py",
        output="screen"
    )

    image_sub_node = Node(
        package="gazebo_env",
        executable="gazebo_image_test.py",
        output="screen"
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["forward_position_controller", "--controller-manager", "/controller_manager"],
    )

    nodes = [
        gazebo_server,
        gazebo_client,
        node_robot_state_publisher,
        spawn_entity,
        joint_state_publisher_node,
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=[
                "0.0",
                "0.0",
                "0.0",  # 0.68
                "-1.571",
                "0.0",  # .33
                "-1.571",
                "camera_link",
                "real_camera_link",
                # "0.35", ##original .50
                # "-0.15", # -.05
                # "0.0", # changed to .55 from .45
                # "0",
                # "0", #original 0
                # "0.0",#1.57
                # "base_link",
                # "camera_link",
            ],
        ),
        #image_sub_node
        #joint_state_broadcaster_spawner,
        #robot_controller_spawner,
    ]

    return LaunchDescription(declared_arguments + nodes)
