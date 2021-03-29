#!/bin/bash
touch /home/pi/startup/mar2420i211052
cd /var/www/html/
/var/www/html/update.sh
cd ~
lxterminal -e /home/pi/startup/startup.sh
