# Abdulrahman Al-Shanoon/Robotics-Course-Projects/Fall2019
#########################################
#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import time
import cv2
import os
import random
from robot import Robot
import utils


# User options (change me)
# --------------- Setup options ---------------
obj_mesh_dir = os.path.abspath('objects')
num_obj = 9
random_seed = 1234
workspace_limits = np.asarray([[-0.62, -0.62], [-1.1,-1.1], [0.3, 0.9]]) # Cols: min max, Rows: x y z (define workspace limits in robot coordinates)
# ---------------------------------------------

# Set random seed
np.random.seed(random_seed)

# Initialize robot simulation
robot = Robot(True, obj_mesh_dir, num_obj, workspace_limits,
              None, None, None, None,
              True, False, None)



# Fetch object poses
obj_positions, obj_orientations = robot.get_obj_positions_and_orientations()


