#!/bin/bash
echo "Run"
sleep 60
date +%c  >> /home/pi/startup/ifconfig.txt
date +%c  >> /home/pi/startup/ping.txt
ifconfig >> /home/pi/startup/ifconfig.txt
ping -c 4 8.8.8.8 >> /home/pi/startup/ping.txt
cd /home/pi/startup
./camera-stream.sh &

while true
do
sleep 60
x=$(( $x+1 ))
echo "Welcome $x times" >> /home/pi/startup/log.txt
done
