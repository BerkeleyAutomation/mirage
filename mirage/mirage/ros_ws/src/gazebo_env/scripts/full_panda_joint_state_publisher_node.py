#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray

class FullPandaJointStatePublisher(Node):
    def __init__(self):
        super().__init__('full_panda_joint_state_publisher')
        self.subscription = self.create_subscription(
            Float64MultiArray,
            '/joint_commands',  # Topic name for /joint_commands
            self.joint_commands_callback,
            10)
        self.publisher = self.create_publisher(
            JointState,
            '/joint_states',  # Topic name for /joint_states
            10)
        self.joint_state_msg = JointState()

    def joint_commands_callback(self, msg):
        # Fill the JointState message with data from the Float64MultiArray
        self.joint_state_msg.header.stamp = self.get_clock().now().to_msg()
        #self.joint_state_msg.name = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint","wrist_1_joint", "wrist_2_joint", "wrist_3_joint","robotiq_85_left_knuckle_joint","robotiq_85_right_knuckle_joint","robotiq_85_left_inner_knuckle_joint","robotiq_85_right_inner_knuckle_joint","robotiq_85_left_finger_tip_joint","robotiq_85_right_finger_tip_joint"]  # Replace with your joint names
        self.joint_state_msg.name = ["panda_joint1", "panda_joint2", "panda_joint3","panda_joint4", "panda_joint5", "panda_joint6","panda_joint7","panda_finger_joint1","panda_finger_joint2"]
        msg.data.append(msg.data[-1])
        #msg.data.append(gripper_val)
        #msg.data.append(gripper_val)
        # for i in range(5):
        #     if(i == 1 or i == 4):
        #         msg.data.append(gripper_val)
        #     else:
        #         msg.data.append(gripper_val)
        self.joint_state_msg.position = msg.data
        self.publisher.publish(self.joint_state_msg)

def main(args=None):
    rclpy.init(args=args)
    full_panda_joint_state_publisher = FullPandaJointStatePublisher()
    rclpy.spin(full_panda_joint_state_publisher)
    full_panda_joint_state_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
