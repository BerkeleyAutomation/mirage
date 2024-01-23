import os
import launch
import launch_ros.actions
import pathlib


def generate_launch_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package="gazebo_env",
                executable="ur5e_point_cloud_publisher.py",
                name="ur5e_point_cloud_publisher",
                output="both",
            )
        ]
    )
