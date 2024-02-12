from subprocess import getoutput, call
from time import sleep
from pathlib import Path
from sys import argv


def main():
    sleep(1)
    output = getoutput(f"pgrep -af '{argv[0]}'").split('\n')
    wallpapers = [
        'wallhaven-1p3ymg_1600x900.png', 'wallhaven-rrd721_1600x900.png'
    ]
    local = Path('~/Imagens/wallpapers/aleatórios').expanduser()
    if len(output) - 1 == 1:
        index = int(getoutput('xdotool get_desktop'))
        local_wallpaper = str(local / wallpapers[index % len(wallpapers)])
        call(f"feh --bg-scale {local_wallpaper}".split())


main()