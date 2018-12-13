# set_walls

#### Requirements
* python3.5 and higher
* feh

#### Python libraries
* os
* random

#### How to

* set wallpapers path
* set monitors list
* start script
###### Attention! You need have subfolders in path

#### Cron init
If you want to init script by crontab, you need to set CRONTAB=true in cron configuration file

example:

    CRONTAB=true
    */1 * * * * /usr/bin/setwallpapers.py >> /var/log/setwallpapers.txt 2>&1
