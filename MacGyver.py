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
from pygame.locals import *
from labyrinth import *
from Donnees import *


def main():
    """Instructions principales"""

    # Initialisaton graphique
    pygame.init()

    # Initialisation du labyrinthe et de l'affichage
    lab_level = Labyrinth(screen_size, grid_file, object_list, ressources_path, step)
    MacGyver = lab_level.init_position

    # Boucle définissant les actions selon les retours clavier
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                MacGyver = lab_level.move_char(MacGyver, 1, 0)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                MacGyver = lab_level.move_char(MacGyver, -1, 0)
            elif event.type == KEYDOWN and event.key == K_DOWN:
                MacGyver = lab_level.move_char(MacGyver, 0, 1)
            elif event.type == KEYDOWN and event.key == K_UP:
                MacGyver = lab_level.move_char(MacGyver, 0, -1)

        lab_level.lab_screen.refresh_screen(lab_level.grid_values)
        

if __name__ == "__main__":
    main()