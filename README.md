Watchdog
========

Watchdog that checks if website is up and does something if down


Changelog:
--------

0.1:
--------
* Initial commit, supports config via json file@/etc/watchdog.conf
* generates logs into /var/log/watchdog.log

Installation
--------
1. Copy watchdog.py to /usr/local/sbin
2. Copy watchdog.conf to /etc/
3. setup a cronjob to run every minute (e.g. * * * * * /usr/python /usr/local/sbin/watchdog.py)