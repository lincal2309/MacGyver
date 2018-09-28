# -*-coding:Utf-8 -*

"""Fichier principal de gestion du jeu de labyrinthe
Les principaux paramètres sopnt stockés dans le fichiers Donnees.py

POINTS A VOIR / A RESOUDRE
- ajuster l'affichage et les images à une fenêtre standard
- Ajouter des messages texte : Accueil du joueur, victoire ou défaite (+ aide ?)
- Gérer les exceptions
- PEP8 / PEP20

"""

import pygame
import sys
from pygame.locals import *
from labyrinth import *
from Donnees import *


def main():
    """Instructions principales"""

    # Initialisaton graphique
    pygame.init()

    lab_data = Donnees()
    # lab_level = Labyrinth(lab_data)
    # MacGyver = lab_level.init_position


    # Boucle définissant les actions selon les retours clavier
    cont_game = True
    while cont_game:
        lab_level = Labyrinth(lab_data)
        MacGyver = lab_level.init_position
        lab_level.lab_screen.display_msg("Dirigez-vous avec les flèches du clavier, ESC pour quitter. Bon jeu !")

        while lab_level.lab_end == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                    MacGyver = lab_level.move_char(MacGyver, 1, 0)
                    # lab_level.lab_screen.refresh_screen(lab_level.grid_values)
                elif event.type == KEYDOWN and event.key == K_LEFT:
                    MacGyver = lab_level.move_char(MacGyver, -1, 0)
                    # lab_level.lab_screen.refresh_screen(lab_level.grid_values)
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    MacGyver = lab_level.move_char(MacGyver, 0, 1)
                    # lab_level.lab_screen.refresh_screen(lab_level.grid_values)
                elif event.type == KEYDOWN and event.key == K_UP:
                    MacGyver = lab_level.move_char(MacGyver, 0, -1)
                    # lab_level.lab_screen.refresh_screen(lab_level.grid_values)
                elif event.type == KEYDOWN and event.key == K_i:
                    lab_level.lab_screen.display_msg("Dirigez-vous avec les flèches du clavier, ESC pour quitter. Bon jeu !")
                


        # if lab_level.lab_end == True:
        #     lab_level.lab_screen.display_msg("Voulez-vous faire une nouvelle partie (O/N) ?")
        
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
            
        # lab_level.lab_screen.refresh_screen(lab_level.grid_values)
        

if __name__ == "__main__":
    main()