#!/usr/bin/env python

import subprocess
from termcolor import colored
import urllib.request

services = {"Plex":"http://192.168.1.3:32400/web/index.html"}


def service_online(link):
    return urllib.request.urlopen("http://192.168.1.3:32400/web/index.html").getcode() == 200


subprocess.call(["figlet", "Dragon Fruit"])
uptime = subprocess.getoutput("uptime -p")
print("Uptime: " + uptime[3:])
user = subprocess.getoutput("whoami")
print("Logged in as: " + user)
subprocess.call(["./system.sh"])
disks = subprocess.getoutput("df -h").split("\n")
for x in range(0, len(disks)):
    if x == 0:
        print(disks[x])
    else:
        disk = ' '.join(disks[x].split()).split(" ")
        if disk[5].startswith("/media") or disk[5] == "/":
            print(disks[x])
            percentage = int(disk[4].replace("%",""))
            num_green_bars = int(percentage / 2)
            green_bar = "=" * num_green_bars
            num_white_bar = 50 - num_green_bars
            white_bar = "=" * num_white_bar

            print("[" + colored(green_bar, 'green') + white_bar + "]")
subprocess.call(["sensors"])

for service in services.keys():
    if service_online(services[service]):
        status = colored(u'\u25CF', 'green') + "online"
    else:
        status = colored(u'\u25B2', 'red') + "offline"
    print(service + ": " + status)