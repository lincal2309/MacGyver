# -*-coding:Utf-8 -*

""" Class gathering all paramters for MacGyver.py programm

    As there is no need to have several instance of this class, it's built as a singleton decorator
"""

import os
import pygame
from observers import *

@singleton
class Donnees:
    def __init__(self):
        # Labyrinth's and window's size
        self.lab_dim = 15 # Number of cels in each direction
        self.cell_size = 40

        # Dimensions of ther screen where the game will be displayed
        self.screen_size = self.screen_height, self.screen_width = pygame.display.Info().current_h, pygame.display.Info().current_w

        # Defines the scale ratio according to the actual output display monitors
        # It includes 1 cell height for displaying message 
        #     and 1 cell for height and width to ensure final display is not right to the screen's borders
        # self.step will be used as final actual cell size
        self.step = min(round(self.screen_height / (self.lab_dim + 2)), round(self.screen_width / (self.lab_dim + 1)))

        # Define scale for objets adjustments when necessary
        self.scale = self.step / self.cell_size

        self.display_size = self.display_width, self.display_height = self.step * self.lab_dim, self.step * (self.lab_dim + 1)

        # Name of the file that defines the grid
        self.grid_file = "grille.txt"

        # List of objects
        self.object_list = ["Seringue", "Aiguille", "Ether"]

        # Pictures folder
        self.ressources_path = "Ressources"

        # List of pictures
        self.MacGyver_file = "MacGyver.png"
        self.Gardian_file = "Gardien.png"
        self.floor_file = "temp_brick_wall.png"
        self.wall_file = "temp_floor_tiles.png"