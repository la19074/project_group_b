#!/usr/bin/env python3
'''
This file contains settings required for maze control and simulation.
'''

# Import modules.
import numpy as np
from math import pi
import pygame

''' PHYSICAL DIMENSIONS '''
# Board dimensions.
FrameSize = np.array([332, 286]) # [mm]
MazeSize = np.array([274.5, 229.5]) # [mm]
FrameHorizontal = (FrameSize[1] - MazeSize[1]) / 2 # [mm]
FrameVertical = (FrameSize[0] - MazeSize[0]) / 2 # [mm]

# Ball dimensions.
BallRadius = 6.335 # [mm]
BallMass = 0.009 # [kg]

# Hole dimensions.
HoleRadius = 7.37 # [mm]

''' CONTROL SETTINGS '''
# Minimum time period of each control loop.
ControlPeriod = 0.2 # [s] (Set to zero.)

# Minimum time period of each graphics loop.
GraphicsPeriod = 0.05 # [s]
"""
# PID Coefficients
Kp = 30e-5
Ki = 0e-5
Kd = 28e-5

# Number of error values to buffer for PID derivative calculation.
BufferSize = 2

# Minimum tilt angle allowed.
MinSignal = np.array([0, 0])

# Maximum motor angle.
SaturationLimit = np.array([pi / 4, pi / 4])
"""

# PID Coefficients
Kp = 30e-5
Ki = 10e-5
Kd = 28e-5

# Number of error values to buffer for PID derivative calculation.
BufferSize = 4

# Minimum tilt angle allowed.
MinSignal = np.array([pi/360, pi/360])

# Maximum motor angle.
SaturationLimit = np.array([pi / 4, pi / 4])


''' SIMULATION SETTINGS '''
# Tilt angle for manual maze tilt.
ThetaStep = 0.01 * pi

# Artificial drag on ball: approximates air resistance and friction.
Drag = 10

# Coefficient of reflectivity off walls. Positive floats0
FrameBounce = 0.06
WallBounce = 0.01

# Simulated +- error value from image detection.
ImageNoise = 2 # [mm]

''' GRAPHICAL SETTINGS '''
# GUI display scaling factor. Use 1 for pi touchscreen.
DisplayScale = 1

# Maze to GUI scaling factor. Don't change.
GUIScale = 1.5 * DisplayScale

# Maze shift for GUI display.
HeaderShift = np.array([0, 51]) * DisplayScale

# Colours
Black      = (0  , 0  , 0  )
White      = (255, 255, 255)
Blue       = (0  , 0  , 255)
Grey       = (169, 169, 169)
DimGrey    = (105, 105, 105)
Red        = (255, 0  , 0  )
Purple     = (75 , 0  , 130)
LightGreen = (80 , 255, 80 )
LightRed   = (255, 100 , 100 )

# Checkpoint Colours
CheckpointColours = {
"SetPoint" : Red,
"Checkpoint" : Blue,
"EndPoint" : Purple
}

# Initialise text module.
pygame.font.init()
# Create fonts.
HeaderFont = pygame.font.SysFont("Times New Roman", 30) # Scaling handled internally.
TextFont = pygame.font.SysFont("Times New Roman", round(20 * DisplayScale))
ButtonFont = pygame.font.SysFont("Times New Roman", 22) # Scaling handled internally.

if __name__ == "__main__":
    import doctest
    doctest.testmod()
