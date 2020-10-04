This script is for checking expiration date of domains and alerting 
Created by Constantine @ 2017 vi127001 [at] gmail.com

How to install:

sudo apt install python3-dateutil python3-pip && sudo -H pip3 install python-whois
git clone https://github.com/constantinekg/check_domain_expiration

How to modify:
Open domainchecker.py in text editor and make changes in global variables section.

How to use:
put script as example into /opt/domainchecker.py
change chmod:
chmod +x /opt/domainchecker.py
put it into crontab (every day at 01:01):
crontab -e
01 01 * * * /opt/domainchecker.py
