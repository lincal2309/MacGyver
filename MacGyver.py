# -*-coding:Utf-8 -*

""" Main file for the labyrinth game
    The main parameters are stored in Donnees.py file
"""

import pygame
import sys
import os
from pygame.locals import *
from labyrinth import *
from Donnees import *


def main():
    """ Main instructions """

    # This environment option makes the windows open in the middle of the screen
    os.environ['SDL_VIDEO_CENTERED'] = "1"

    pygame.init()

    lab_data = Donnees()


    # Main loop to manage several games the user can play
    cont_game = True
    while cont_game:
        lab_level = Labyrinth(lab_data)
        MacGyver = lab_level.init_position
        lab_level.lab_screen.display_msg("Dirigez-vous avec les flèches du clavier, ESC pour quitter. Bon jeu !")

        # Game loop to capture player's events (keybord actions)
        while lab_level.lab_end == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                    MacGyver = lab_level.move_char(MacGyver, 1, 0)
                elif event.type == KEYDOWN and event.key == K_LEFT:
                    MacGyver = lab_level.move_char(MacGyver, -1, 0)
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    MacGyver = lab_level.move_char(MacGyver, 0, 1)
                elif event.type == KEYDOWN and event.key == K_UP:
                    MacGyver = lab_level.move_char(MacGyver, 0, -1)
                elif event.type == KEYDOWN and event.key == K_i:
                    lab_level.lab_screen.display_msg("Dirigez-vous avec les flèches du clavier, ESC pour quitter. Bon jeu !")
                
        # Loop for end of game actions, waiting for user's decision to quit or restart
        ask_other_game = True
        while ask_other_game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_o:
                    lab_level.lab_end = False
                    ask_other_game = False
                elif event.type == KEYDOWN and event.key == K_n:
                    cont_game = False
                    ask_other_game = False

if __name__ == "__main__":
    main()