#!/usr/bin/env python3
'''
This file stores the Maze objects for Maze 1,2 and 3.
'''

# Import modules.
import numpy as np

# Import objects and settings.
from simulation.objects import CircleMaze
from objects import Maze, Ball, Checkpoint
from settings import FrameSize, MazeSize

# Calculate width of frame side.
FrameSide = (FrameSize - MazeSize) / 2

''' MAZE 1 START '''
Ball1 = Ball(np.array([FrameSide[0] + 123, FrameSide[1] + 8]))

Maze1 = Maze(Ball1, [], [], [])

Maze1Points = ((123, 9),(90, 9), (11, 9), (11, 40), (11, 70), (21, 86), (61, 72), (80, 75), (92, 81), (101, 89), (103, 100), (103, 110), (102, 122), (94, 130), (84, 134), (69, 134), (55, 131), (46, 130), (36, 133), (32, 139), (29, 144), (28, 148), (26, 151), (24, 154), (22, 157), (20, 162), (17, 166), (15, 169), (14, 173), (15, 175), (15, 197), (33, 199), (49, 199), (65, 197), (65, 183), (65, 170), (78, 168), (90, 169), (91, 180), (93, 191), (106, 191), (123, 189), (122, 178), (123, 169), (145, 168), (162, 169), (171, 167), (172, 151), (171, 141), (166, 138), (157, 137), (150, 136), (144, 136), (140, 136), (136, 133), (134, 130), (132, 127), (131, 123), (131, 118), (132, 113), (135, 108), (138, 104), (142, 101), (149, 98), (159, 93), (170, 87), (184, 82), (194, 75), (198, 69), (199, 64), (201, 58), (199, 52), (196, 43), (191, 37), (186, 33), (182, 30), (180, 24), (181, 17), (187, 12), (208, 12), (220, 12), (231, 22), (245, 30), (251, 37), (248, 48), (248, 57), (252, 65), (255, 69), (258, 74), (260, 77), (260, 83), (261, 87), (259, 94), (256, 98), (253, 102), (248, 106), (243, 112), (241, 114), (239, 119), (238, 122), (239, 127), (240, 131), (245, 134), (247, 136), (250, 139), (254, 141), (259, 145), (262, 149), (262, 157), (263, 164), (263, 171), (261, 178), (259, 184), (257, 188), (253, 192), (250, 194), (244, 196), (239, 196), (234, 195), (229, 193), (224, 190), (216, 185), (209, 182), (205, 189), (203, 200), (199, 213), (192, 218), (163, 218), (137, 218), (109, 218), (96, 219))

for Point in Maze1Points:
    Coordinates = np.array([Point[0], Point[1]]) + FrameSide
    Checkpoint_ = Checkpoint(Coordinates)
    Maze1.Checkpoints.append(Checkpoint_)
''' MAZE 1 END '''

''' MAZE 2 START '''
Ball2 = Ball(np.array([FrameSide[0] + 158, FrameSide[1] + 12]))

Maze2 = Maze(Ball2, [], [], [])

Maze2Points = ((158, 12), (119, 12), (88, 12), (57, 12), (56, 37), (56, 54), (56, 60), (57, 66), (59, 70), (61, 73), (63, 75), (66, 77), (68, 79), (71, 82), (72, 87), (73, 94), (73, 100), (74, 106), (73, 111), (71, 117), (68, 120), (65, 123), (60, 125), (55, 126), (49, 128), (41, 129), (33, 131), (26, 133), (21, 135), (18, 140), (15, 145), (14, 152), (14, 159), (14, 175), (16, 184), (21, 187), (26, 187), (31, 186), (38, 183), (44, 180), (48, 177), (54, 175), (60, 172), (68, 170), (75, 169), (82, 169), (82, 164), (83, 158), (84, 147), (90, 146), (97, 146), (103, 146), (110, 146), (116, 146), (119, 146), (119, 153), (119, 161), (119, 168), (119, 175), (119, 182), (120, 186), (129, 186), (140, 186), (144, 184), (144, 174), (143, 164), (143, 156), (144, 145), (143, 137), (141, 133), (137, 128), (134, 124), (130, 119), (125, 114), (122, 110), (119, 106), (114, 104), (108, 101), (103, 98), (101, 93), (99, 88), (98, 81), (99, 74), (99, 65), (99, 53), (98, 45), (99, 38), (99, 35), (104, 35), (110, 35), (115, 35), (121, 35), (126, 35), (128, 38), (128, 46), (129, 51), (134, 52), (141, 51), (146, 51), (150, 51), (155, 52), (163, 51), (171, 51), (181, 51), (190, 49), (194, 45), (195, 42), (198, 38), (199, 35), (203, 31), (206, 30), (211, 28), (218, 28), (227, 28), (239, 29), (249, 29), (258, 30), (259, 38), (259, 53), (253, 55), (246, 55), (242, 55), (238, 56), (235, 58), (232, 60), (230, 64), (227, 67), (225, 71), (222, 75), (220, 77), (219, 80), (214, 83), (208, 85), (203, 89), (198, 91), (192, 94), (188, 97), (183, 99), (180, 100), (177, 102), (175, 104), (174, 107), (173, 112), (173, 117), (173, 126), (173, 132), (180, 133), (192, 133), (194, 138), (194, 145), (194, 151), (197, 156), (203, 161), (209, 169), (214, 177), (215, 188), (215, 198), (216, 208), (215, 213), (200, 213), (178, 213), (150, 213), (129, 213), (117, 213), (107, 213))

for Point in Maze2Points:
    Coordinates = np.array([Point[0], Point[1]]) + FrameSide
    Checkpoint_ = Checkpoint(Coordinates)
    Maze2.Checkpoints.append(Checkpoint_)
''' MAZE 2 END '''

"""
''' MAZE 3 START '''
Ball3 = Ball(np.array([FrameSide[0] + 142, FrameSide[1] + 17]))

Maze3 = Maze(Ball3, [], [], [])

Maze3Points = ((142, 17), (128, 17), (112, 17), (99, 17), (85, 17), (83, 18), (83, 22), (82, 26), (81, 29), (78, 30), (74, 31), (69, 31), (66, 31), (64, 30), (62, 29), (61, 25), (60, 21), (59, 17), (54, 16), (49, 15), (40, 15), (38, 18), (38, 23), (38, 28), (38, 32), (37, 33), (35, 34), (32, 35), (26, 35), (20, 35), (17, 35), (15, 37), (15, 48), (15, 59), (15, 63), (21, 63), (27, 63), (32, 63), (36, 63), (38, 66), (39, 70), (39, 77), (38, 81), (28, 82), (21, 82), (15, 83), (15, 90), (15, 96), (15, 101), (18, 103), (22, 102), (27, 102), (33, 102), (38, 103), (40, 103), (40, 108), (40, 117), (40, 124), (39, 133), (39, 136), (31, 137), (24, 137), (18, 138), (16, 139), (15, 141), (16, 146), (16, 153), (16, 158), (17, 161), (21, 165), (25, 168), (31, 171), (33, 176), (35, 179), (35, 183), (31, 186), (29, 191), (27, 193), (26, 197), (24, 200), (24, 205), (24, 210), (25, 213), (28, 215), (36, 215), (45, 215), (54, 215), (58, 212), (60, 209), (64, 206), (68, 202), (71, 200), (75, 196), (80, 191), (84, 188), (87, 184), (87, 180), (87, 174), (85, 172), (83, 170), (80, 168), (76, 167), (72, 167), (69, 166), (67, 161), (67, 157), (67, 153), (72, 149), (75, 145), (78, 143), (83, 143), (91, 143), (97, 142), (103, 142), (106, 141), (107, 137), (106, 131), (107, 127), (107, 122), (107, 113), (107, 110), (106, 105), (104, 103), (99, 103), (93, 103), (89, 103), (86, 102), (82, 100), (79, 98), (75, 95), (71, 93), (68, 90), (64, 88), (62, 86), (62, 81), (62, 75), (62, 71), (62, 67), (63, 62), (67, 62), (74, 62), (79, 62), (86, 62), (92, 62), (98, 62), (104, 62), (107, 61), (106, 56), (106, 52), (107, 48), (107, 45), (107, 41), (113, 40), (120, 40), (125, 40), (128, 42), (129, 50), (127, 58), (128, 63), (128, 68), (130, 70), (132, 70), (136, 70), (141, 70), (145, 70), (148, 71), (149, 75), (149, 80), (149, 85), (149, 89), (149, 94), (149, 97), (149, 100), (148, 101), (146, 103), (145, 103), (142, 104), (139, 105), (134, 105), (130, 105), (128, 107), (127, 110), (127, 114), (127, 117), (127, 121), (128, 125), (128, 128), (129, 133), (129, 136), (131, 138), (135, 138), (140, 138), (146, 138), (149, 138), (148, 142), (149, 146), (150, 150), (150, 153), (147, 155), (142, 156), (137, 156), (132, 157), (130, 157), (127, 160), (127, 165), (127, 168), (127, 171), (127, 174), (124, 175), (119, 176), (113, 176), (107, 177), (106, 185), (107, 192), (106, 202), (107, 212), (117, 212), (126, 212), (137, 212), (147, 212), (150, 211), (150, 208), (150, 204), (150, 198), (150, 193), (150, 188), (150, 185), (155, 183), (158, 180), (161, 179), (164, 177), (166, 175), (168, 173), (172, 172), (178, 172), (182, 172), (186, 172), (189, 172), (193, 173), (192, 181), (193, 190), (193, 199), (194, 207), (193, 213), (202, 212), (212, 213), (215, 212), (215, 205), (215, 196), (215, 186), (215, 184), (220, 183), (226, 183), (231, 182), (237, 182), (241, 182), (243, 179), (248, 175), (252, 171), (255, 168), (255, 162), (252, 158), (249, 154), (246, 151), (242, 149), (239, 145), (236, 141), (235, 135), (235, 130), (235, 123), (234, 117), (230, 115), (223, 115), (218, 116), (215, 116), (214, 118), (213, 126), (213, 133), (214, 137), (214, 142), (212, 144), (203, 145), (195, 144), (192, 139), (192, 134), (192, 131), (184, 131), (178, 131), (173, 132), (170, 130), (171, 122), (170, 117), (170, 112), (170, 108), (174, 106), (177, 103), (180, 99), (184, 96), (188, 93), (191, 90), (194, 87), (195, 86), (199, 86), (205, 85), (210, 85), (212, 84), (213, 81), (213, 78), (213, 76), (213, 72), (213, 70), (210, 69), (206, 68), (202, 68), (197, 68), (193, 68), (192, 62), (192, 59), (192, 48), (193, 34), (193, 32), (204, 31), (210, 30), (213, 30), (217, 30), (222, 30), (227, 31), (230, 31), (233, 31), (235, 34), (237, 37), (238, 41), (238, 46), (238, 50), (238, 56), (237, 60), (238, 65), (238, 69), (238, 71), (240, 72), (244, 72), (249, 72), (253, 73), (257, 73), (256, 79), (256, 82), (255, 95), (256, 105), (256, 117))

for Point in Maze3Points:
    Coordinates = np.array([Point[0], Point[1]]) + FrameSide
    Checkpoint_ = Checkpoint(Coordinates)
    Maze3.Checkpoints.append(Checkpoint_)
''' MAZE 3 END '''
"""

''' MAZE 3 START '''
Ball3 = Ball(np.array([FrameSide[0] + 142, FrameSide[1] + 17]))

Maze3 = Maze(Ball3, [], [], [])

# Please replace these with the actual mazes.
Maze3Points = ((135, 9), (4, 3), (4, 108), (30, 107), (108, 63), (109, 146), (58, 147), (50, 119), (3, 184), (4, 224), (68, 224), (98, 160), (132, 198), (178, 124), (122, 146), (123, 81), (219, 51), (163, 4), (271, 4), (271, 50), (232, 67), (271, 113), (233, 149), (271, 224), (222, 222), (192, 164), (194, 222), (84, 220))

for Point in Maze3Points:
    Coordinates = np.array([Point[0], Point[1]]) + FrameSide
    Checkpoint_ = Checkpoint(Coordinates)
    Maze3.Checkpoints.append(Checkpoint_)
''' MAZE 3 END '''

if __name__ == "__main__":
    if type(Maze1) != Maze:
        raise TypeError("Maze1 should be of class Maze. See 'objects.py'.")
    elif type(Maze2) != Maze:
        raise TypeError("Maze2 should be of class Maze. See 'objects.py'.")
    elif type(Maze3) != Maze:
        raise TypeError("Maze3 should be of class Maze. See 'objects.py'.")
