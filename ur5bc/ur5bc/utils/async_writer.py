import threading
import os 
from PIL import Image
import numpy as np
import cv2

class AsyncWrite(threading.Thread):
    '''
    Saving images only
    '''
    def __init__(self, hand_image, third_person_image_color, third_person_image_depth, traj_index, saving_directory, i, front=False):
        # calling superclass init
        threading.Thread.__init__(self)
        self.hand_image = hand_image
        self.third_person_image_color = third_person_image_color
        self.third_person_image_depth = third_person_image_depth
        self.traj_index = traj_index
        self.saving_directory = saving_directory
        self.i = i
        self.front = front
        os.makedirs(os.path.join(saving_directory, f"traj{traj_index}", "images"), exist_ok=True)

    def run(self):
        if not self.front:
            if self.hand_image is not None:
                # cv2.imwrite(os.path.join(self.saving_directory, f"traj{self.traj_index}", "images", f"hand_img_{self.i}.png"), self.hand_image)
                Image.fromarray(self.hand_image).save(os.path.join(self.saving_directory, f"traj{self.traj_index}", "images", f"inpainted_{self.i}.png"))

            Image.fromarray(self.third_person_image_color).save(os.path.join(self.saving_directory, f"traj{self.traj_index}", "images", f"raw_{self.i}.png"))

            # with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "images", "third_person_img_depth_%d.npy" % self.i), 'wb') as f:
            #     np.save(f, self.third_person_image_depth)
            
        else:
            if self.hand_image is not None:
                # cv2.imwrite(os.path.join(self.saving_directory, f"traj{self.traj_index}", "images", f"hand_img_{self.i}.png"), self.hand_image)
                Image.fromarray(self.hand_image).save(os.path.join(self.saving_directory, f"traj{self.traj_index}", "images", f"inpainted_front_{self.i}.png"))

            Image.fromarray(self.third_person_image_color).save(os.path.join(self.saving_directory, f"traj{self.traj_index}", "images", f"raw_front_{self.i}.png"))

            # with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "images", "third_person_img_depth_%d.npy" % self.i), 'wb') as f:
            #     np.save(f, self.third_person_image_depth)
        
class AsyncWriteStandardizedFormat(threading.Thread):
    '''
    Save all data in the standardized format
    '''
    def __init__(self, robot_state, action, image, traj_index, saving_directory, i):
        # calling superclass init
        threading.Thread.__init__(self)
        self.robot_state = robot_state
        self.action = action
        self.image = image
        self.traj_index = traj_index
        self.saving_directory = saving_directory
        self.i = i

    def run(self):
        if self.i == 0:
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "robot_state.npy" % self.i), 'wb') as f:
                np.save(f, np.array(self.robot_state))
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "action.npy" % self.i), 'wb') as f:
                np.save(f, np.array(self.action))
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "image.npy" % self.i), 'wb') as f:
                np.save(f, np.array(self.image))
        else:
            # read the previous state
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "robot_state.npy" % (self.i-1)), 'rb') as f:
                prev_robot_state = np.load(f)
            # append the latest state
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "robot_state.npy" % self.i), 'wb') as f:
                np.save(f, np.vstack((prev_robot_state, np.array(self.robot_state))))
            # read the previous action
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "action.npy" % (self.i-1)), 'rb') as f:
                prev_action = np.load(f)
            # append the latest action
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "action.npy" % self.i), 'wb') as f:
                np.save(f, np.vstack((prev_action, np.array(self.action))))
            # read the previous image
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "image.npy" % (self.i-1)), 'rb') as f:
                prev_image = np.load(f)
            # append the latest image
            with open(os.path.join(self.saving_directory, f"traj{self.traj_index}", "image.npy" % self.i), 'wb') as f:
                np.save(f, np.vstack((prev_image, np.array(self.image))))

        

        