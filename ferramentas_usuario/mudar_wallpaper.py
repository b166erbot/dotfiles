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

# alias
#set $feh exec --no-startup-id feh --bg-scale

# switch workspace
#bindsym $mod+1 workspace 1 ; $feh ~/wp/1.jpg
#bindsym $mod+2 workspace 2 ; $feh ~/wp/2.jpg
#bindsym $mod+3 workspace 3 ; $feh ~/wp/3.jpg
#bindsym $mod+4 workspace 4 ; $feh ~/wp/4.jpg
#bindsym $mod+5 workspace 5 ; $feh ~/wp/5.jpg
#bindsym $mod+6 workspace 6 ; $feh ~/wp/6.jpg
#bindsym $mod+7 workspace 7 ; $feh ~/wp/7.jpg
#bindsym $mod+8 workspace 8 ; $feh ~/wp/8.jpg
#bindsym $mod+9 workspace 9 ; $feh ~/wp/9.jpg
#bindsym $mod+0 workspace 10 ; $feh ~/wp/10.jpg