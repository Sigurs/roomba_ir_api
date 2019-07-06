#!/bin/bash

# Make sure only root can run our script
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Update
apt update && apt upgrade -y

# Install lirc
apt install lirc -y

# Configuration of lirc is platform specific, so not including here. Do it yourself.
##Enable service
#systemctl enable lircd.socket lircd.service
#systemctl start lircd.socket lircd.service
#
## RaspberryPi specific. Enable gpio-ir-tx
#echo "dtoverlay=gpio-ir-tx,gpio_in_pin=23,gpio_out_pin=22" >> /boot/config.txt


# Add user.
useradd roomba_api