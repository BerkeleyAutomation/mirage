import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from control_msgs.action import GripperCommand

#from action_tutorials_interfaces.action import Fibonacci


class GripperClient(Node):

    def __init__(self):
        super().__init__('gripper_action_client')
        self._action_client = ActionClient(self, GripperCommand, '/robotiq_gripper_controller/gripper_cmd')

    def send_goal(self):
        goal_msg = GripperCommand.Goal()
        goal_msg.command.position = 0.4
        goal_msg.command.max_effort = 10.0
        print(goal_msg.command)
        print("I'm HIM")
        # goal_msg.order = order

        self._action_client.wait_for_server()
        print("WE HERE")

        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = GripperClient()

    future = action_client.send_goal()

    rclpy.spin_until_future_complete(action_client, future)

    print("COOK")


if __name__ == '__main__':
    main()