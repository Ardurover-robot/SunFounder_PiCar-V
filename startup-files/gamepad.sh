#!/bin/bash
cd /var/www/html
mkdir gamepad
cd gamepad
touch gamepad.py
#Installed evdev to work with this python script.
#use sudo sudo pip install evdev to install the required library on the raspberry pi.
#Once the controller arrives tomorrow, I'll run 
#python /usr/local/lib/python2.7/dist-packages/evdev/evtest.py
#to make sure it works.
ls /dev/input/ > /var/www/html/gamepad/dev.txt

lxterminal -e python gamepad.py 
scrot /var/www/html/screen.jpg
