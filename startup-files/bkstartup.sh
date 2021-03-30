#!/bin/bash
touch /home/pi/startup/mar2420i211052
cd /var/www/html/
echo "Today's date is: $(date)"
day=$(date +"%u")

if ((day > 5)); then
/var/www/html/update.sh
else
   echo "WORKING DAY"
fi
cd ~
lxterminal -e /home/pi/startup/startup.sh
