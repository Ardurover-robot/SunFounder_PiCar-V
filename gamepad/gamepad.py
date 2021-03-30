#Created by Kepler Electronics, https://www.youtube.com/keplerelectronics
import explorerhat
import os
import time

explorerhat.motor.one.invert()

from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event0')
print(gamepad)



for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        if event.code == 0:
            if event.value == 0:
                
                print("Left");#explorerhat.motor.one.forwards(event.value-155)
            elif event.value == 2:
                print("Right");#explorerhat.motor.one.backwards((100-event.value))
            else:
                explorerhat.motor.one.stop()
        elif event.code == 1:
            if event.value == 0:
                print("Up");#explorerhat.motor.two.forwards(event.value-155)
            elif event.value == 2:
                print("Down");#explorerhat.motor.two.backwards((100-event.value))
            else:
                explorerhat.motor.two.stop()

