#!/bin/bash
tail ~/.config/lxsession/LXDE-pi/autostart > /var/www/html/autostart
mkdir /var/www/html/startup-files;cp ~/startup/* /var/www/html/startup-files/
