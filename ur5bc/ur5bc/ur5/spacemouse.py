import time
import numpy as np
import pyspacemouse
import threading

class SpaceMouseRobotController:
    def __init__(self):
        self.current_action = np.zeros(6)
        self.button_0_pressed = False
        self.button_1_pressed = False
        # self.read_device()
        # launch a new listener thread to listen to SpaceMouse
        self.thread = threading.Thread(target=self.read_device)
        self.thread.daemon = True
        self.thread.start()

    def send_action_to_robot(self, action):
        # Replace this method with your robot control API
        # For example:
        # self.robot.set_velocity(action)
        # print("Current action sent to robot:", action)
        print("Current action sent to robot:", action)
        pass

    def read_device(self):

        button_arr = [pyspacemouse.ButtonCallback(0, self.button_0), # this is called whenever the button state changes and if button 0 is being pressed after the state change
                    pyspacemouse.ButtonCallback(1, self.button_1), # this is called whenever the button state changes and if button 1 is being pressed after the state change
                    pyspacemouse.ButtonCallback([0, 1], self.button_0_1), ] # this is called whenever the button state changes and if both buttons is being pressed after the state change

        # device = pyspacemouse.open(dof_callback=pyspacemouse.print_state, button_callback=self.someButton, button_callback_arr=button_arr)
        device = pyspacemouse.open(button_callback=self.someButton, button_callback_arr=button_arr)
        if device is not None:
            while True:
                self.state = device.read() # state: {t,x,y,z,pitch,yaw,roll,button} namedtuple
                # print(state.x, state.y, state.z, state.roll, state.pitch, state.yaw)
                self.current_action = np.array([self.state.x, self.state.y, self.state.z, self.state.roll, self.state.pitch, self.state.yaw])
                # time.sleep(0.01)
                # self.current_action[3] = state.yaw * (np.abs(state.yaw) > 0.8)
                # if np.isclose(self.current_action[3], 0):
                #     self.current_action[0] = np.cos(np.pi/4) * state.y - np.sin(np.pi/4) * state.x
                #     self.current_action[1] = -np.sin(np.pi/4) * state.y - np.cos(np.pi/4) * state.x
                #     if not (state.x > 0.8 and state.y > 0.8):
                #         self.current_action[2] = state.z
                #     # self.current_action[5] = -state.yaw
                
                # self.send_action_to_robot(self.current_action)
                # time.sleep(0.1)
        else:
            print("Failed to open spacemouse device")

    def someButton(self, state, buttons):
        """
        This function is called whenever the button state changes. This is called before the button callback array
        """
        print("Some button")

    def button_0(self, state, buttons, pressed_buttons):
        """
        state: SpaceNavigator(t=93844.164859684, x=0, y=0, z=0, roll=0, pitch=0, yaw=0, buttons=[1, 0])
        buttons: [1, 0] # whether each button is pressed
        pressed_buttons= 0 # index of buttons that is pressed
        """
        print("Button 0 is pressed")
        self.button_0_pressed = True
        time.sleep(0.1999)
        self.button_0_pressed = False

    def button_1(self, state, buttons, pressed_buttons):
        """
        state: SpaceNavigator(t=93844.164859684, x=0, y=0, z=0, roll=0, pitch=0, yaw=0, buttons=[1, 0])
        buttons: [1, 0] # whether each button is pressed
        pressed_buttons= 1 # index of buttons that is pressed
        """
        print("Button 1 is pressed")
        self.button_1_pressed = True
        time.sleep(0.2999)
        self.button_1_pressed = False


    def button_0_1(self, state, buttons, pressed_buttons):
        print("Buttons 0 and 1 are pressed")




    

if __name__ == "__main__":
    controller = SpaceMouseRobotController()
    time.sleep(0.1)
    while True:
        print(controller.state)

