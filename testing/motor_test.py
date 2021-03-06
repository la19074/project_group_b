#!/usr/bin/env python3
'''
This file contains functions used to test and calibrate the motor control function.
'''

# Import modules.
import numpy as np
from math import pi
from time import sleep, perf_counter

# Import functions.
from motor_control.motor_control import motor_angle, motor_reset
from motor_control.motor_control_2 import MotorController

def test1():
    motor_reset()
    LastTime = perf_counter()
    motor_angle(np.array([-pi / 4, -pi / 4]))
    TimeStep = perf_counter() - LastTime
    print(round(TimeStep * 1000, 2))
    sleep(1)
    LastTime = perf_counter()
    motor_angle(np.array([0, 0]))
    TimeStep = perf_counter() - LastTime
    print(round(TimeStep * 1000, 2))
    sleep(1)
    LastTime = perf_counter()
    motor_angle(np.array([pi / 4, pi / 4]))
    TimeStep = perf_counter() - LastTime
    print(round(TimeStep * 1000, 2))

def test2():
    MotorController_ = MotorController()
    MotorController_.start()
    LastTime = perf_counter()
    MotorController_.change_angle(np.array([-pi / 4, -pi / 4]))
    TimeStep = perf_counter() - LastTime
    print(round(TimeStep * 1000, 2))
    sleep(1)
    LastTime = perf_counter()
    MotorController_.change_angle(np.array([0, 0]))
    TimeStep = perf_counter() - LastTime
    print(round(TimeStep * 1000, 2))
    sleep(1)
    LastTime = perf_counter()
    MotorController_.change_angle(np.array([pi / 4, pi / 4]))
    TimeStep = perf_counter() - LastTime
    print(round(TimeStep * 1000, 2))
    sleep(5)
    MotorController_.stop()

def test3():
    motor_reset()
    LastTime = perf_counter()
    motor_angle(np.array([0, 0]))
    TimeStep = perf_counter() - LastTime
    print(round(TimeStep * 1000, 2))
    sleep(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
