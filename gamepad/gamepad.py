#Modified code from here: https://github.com/sunfounder/SunFounder_PiCar-V/blob/master/ball_track/ball_tracker.py
#Created by Kepler Electronics, https://www.youtube.com/keplerelectronics
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
import time
from time import sleep
import numpy as np
import picar #a second time?
import os
from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice('/dev/input/event0')
print(gamepad)
turnServo = Servo.Servo(0);
picar.setup()
bw = picar.back_wheels.Back_Wheels()
speedup = 0
bw.forward()
bw.speed = 50 
time.sleep(5)
bw.stop()
for event in gamepad.read_loop():
    print(event.code)
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
                bw.backward() 
                speedup = 100 
                print("Up");#explorerhat.motor.two.forwards(event.value-155)
            elif event.value == 2:
                bw.forward() 
                speedup = 100 
                print("Down");#explorerhat.motor.two.backwards((100-event.value))
            else:
                bw.stop()#turnServo.write(0);
                speedup = 0 
                #explorerhat.motor.two.stop()
                print("Stop")
    elif event.code == 310:
        speedup = speedup + 10
        print("Upp")
    elif event.code == 311:
        speedup = speedup - 10
        print("Doown")

    if(speedup <= 100):
        if(speedup >= 0):
            bw.speed = speedup


