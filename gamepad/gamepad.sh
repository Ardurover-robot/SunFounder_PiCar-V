#!/bin/bash
while True
do
cd /var/www/html/gamepad
python gamepad.py
sleep 1
echo "******* LOG ********"
scrot /var/www/html/screen.jpg
sleep 10
done
