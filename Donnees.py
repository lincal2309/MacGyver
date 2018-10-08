# -*-coding:Utf-8 -*

""" Class gathering all paramters for MacGyver.py programm

    As there is no need to have several instance of this class, it's built as a singleton decorator
"""

import os
from observers import *

@singleton
class Donnees:
    def __init__(self):
        # Labyrinth's and window's size
        self.lab_dim = 15
        self.step = 60 # A REVOIR - variable de pas pour gérer le déplacement - dépend de la taille de simages et de la grille
        self.screen_size = self.screen_width, self.screen_height = self.step * self.lab_dim, self.step * (self.lab_dim + 1)

        # Name of the file that defines the grid
        self.grid_file = "grille.txt"

        # List of objects
        self.object_list = ["Seringue", "Aiguille", "Ether"]

        # Pictures folder
        self.ressources_path = os.path.dirname(".\\Ressources\\")

        # List of pictures
        self.MacGyver_file = "MacGyver.png"
        self.Gardian_file = "Gardien.png"
        self.floor_file = "temp_brick_wall.png"
        self.wall_file = "temp_floor_tiles.png"