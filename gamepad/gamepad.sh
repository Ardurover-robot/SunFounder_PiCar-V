#!/bin/bash
cd /var/www/html/gamepad
python gamepad.py
sleep 1
echo "******* LOG ********"
scrot /var/www/html/screen.jpg
sleep 30
