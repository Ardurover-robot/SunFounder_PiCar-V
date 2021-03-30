#Modified code from here: https://github.com/sunfounder/SunFounder_PiCar-V/blob/master/ball_track/ball_tracker.py
#Created by Kepler Electronics, https://www.youtube.com/keplerelectronics
#import explorerhat
#import os
#import time
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep
#import cv2
import numpy as np
import picar #a second time?
import os

#explorerhat.motor.one.invert()

from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event0')
print(gamepad)

turnServo = Servo.Servo(0);
picar.setup()
bw = picar.back_wheels.Back_Wheels()
speedup = 0;
acc = 0




for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        if event.code == 0:
            if event.value == 0:
                turnServo.write(60); 
                print("Left");#explorerhat.motor.one.forwards(event.value-155)
            elif event.value == 2:
                turnServo.write(110); 
                print("Right");#explorerhat.motor.one.backwards((100-event.value))
            else:
                turnServo.write(80);
                #explorerhat.motor.one.stop()
        elif event.code == 1:
            if event.value == 0:
                acc = 7 
                speedup = 35 
                print("Up");#explorerhat.motor.two.forwards(event.value-155)
            elif event.value == 2:
                acc = 4 
                speedup = 35
                print("Down");#explorerhat.motor.two.backwards((100-event.value))
            else:
                bw.stop()#turnServo.write(0);
                #explorerhat.motor.two.stop()
                print("Stop")
    if(speedup < 100):
        speedup = speedup + acc
    speedup = speedup - 1
    if(acc == 7):
        bw.backward()
    if(acc == 4):
        bw.forward()
    if(speedup < 100):
        bw.speed = speedup

