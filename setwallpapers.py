#!/usr/bin/python
from os import listdir, getenv
from os.path import isfile, join, isdir
import random
import subprocess

######################################
##############SETTING#################
######################################

wallpapers_path = "/server/WALLPAPERS/four_monitors"
debug = False
randomize = True

# Key - monitor name (for usability, you can name it as you wish)
# Value - subfolder in wallpapers path
monitors_list = {
    "DP-3": "1",
    "DVI-I-1": "4",
    "DP-5": "2",
    "HDMI-0": "2",
}
feh_type = "bg-scale"

######################################
###########CODE OF LIB################
######################################

wallpapers = {}


def get_wallpapers_list():
    wallpapers_dirs_list = [
        f for f
        in listdir(wallpapers_path)
        if isdir(join(wallpapers_path, f))
    ]
    print(wallpapers_dirs_list)
    for wallpapers_dir in wallpapers_dirs_list:
        wallpapers[wallpapers_dir] = [
            f for f
            in listdir(join(wallpapers_path, wallpapers_dir))
           if isfile(join(wallpapers_path, wallpapers_dir, f))
        ]
    print(wallpapers)


def set_wallpapers():
    feh_wallpapers = []
    for monitor, folder in monitors_list.items():
        feh_wallpapers.append(get_wallpaper_from_path(feh_wallpapers, folder))
    print(feh_wallpapers)

    command = f"feh --{feh_type} {' '.join(feh_wallpapers)}"

    if getenv("CRONTAB") == 'true':
        command = 'export DISPLAY=:0; ' + command

    print(command)
    result = subprocess.check_output(
        [command],
        shell=True
    )
    print(result)


def get_wallpaper_from_path(wallpapers_list, path):
    print(wallpapers_list)
    if randomize:
        wallpaper_to_append = random.choice(wallpapers[path])
    else:
        wallpaper_to_append = wallpapers_list[path][0]

    wallpaper_to_append = join(wallpapers_path, path, wallpaper_to_append)

    if wallpaper_to_append in wallpapers_list:
        wallpaper_to_append = get_wallpaper_from_path(wallpapers_list, path)

    return wallpaper_to_append


if debug:
    from pprint import pprint as print
else:
    def print(*args, **kwargs):
        pass


if __name__ == "__main__":
    get_wallpapers_list()
    set_wallpapers()
