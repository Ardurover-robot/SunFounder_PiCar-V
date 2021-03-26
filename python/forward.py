#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

MotorPin1 = 17
MotorPin2 = 18
MotorEnable = 27

GPIO.output(MotorEnable, GPIO.HIGH)
GPIO.output(MotorPin1, GPIO.HIGH)
GPIO.output(MotorPin2, GPIO.HIGH)
time.sleep(5)
GPIO.output(MotorEnable, GPIO.LOW)
GPIO.output(MotorPin1, GPIO.LOW)
GPIO.output(MotorPin2, GPIO.LOW)
