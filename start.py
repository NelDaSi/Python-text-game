from time import sleep
# import world_check
import textimg
import sys
from random import uniform
# import game
import os
# import player


def play_intro():
    # loading()
    print("*Beep* *Boop*")
    # player_name = player.get_player_name()
    # print(player_name)
    sleep(5.0)


def loading():
    loading_bar = "███████████████████████████████████████████████████████████"
    print(textimg.Loading())
    for x in loading_bar:
        print(x, end='')
        sys.stdout.flush()
        # sleep(0.05)
        # __Random typing speed__
        sleep(uniform(0.05, 0.2))
    os.system('cls')
    return
