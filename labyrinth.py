# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
from random import randint, choice
from observers import *
from screen import *


class Labyrinth:
    """ This class manages labyrinth's levels (only one in our case) """

    def __init__(self, lab_data):
        self.lab_data = lab_data
        self.lab_end = False
        self.lab_screen = Screen(self.lab_data)

        # All pictures are load once - avoid multiple load if this instruction is pu in the main loop
        self.MacGyver_img = load_image(self.lab_data.MacGyver_file, self.lab_data.ressources_path, self.lab_data.step)
        self.Gardian_img = load_image(self.lab_data.Gardian_file, self.lab_data.ressources_path, self.lab_data.step)
        self.floor_img = load_image(self.lab_data.floor_file, self.lab_data.ressources_path, self.lab_data.step, False)
        self.wall_img = load_image(self.lab_data.wall_file, self.lab_data.ressources_path, self.lab_data.step)

        # Grid initialisation thanks to the dedicated method
        self.init_position, self.inventory, self.grid_values = \
            self.def_grid_values(self.lab_data.object_list, self.lab_data.ressources_path, self.lab_data.step)

    
    def def_grid_values(self, object_list, ressources_path, step):
        """ Grid initialisation method
            - Build the grid according to the pattern desinged in the grid file
            - Define what is at each place
        """
        
        # Read the grid definition file
        init_position = ()   # MacGyver's initial place
        grid_values = {}     # Dictionary of the places. Key : position in the grid (X, y)
        f = open(self.lab_data.grid_file, "r")
        cont = f.read()
        for l, line in enumerate(cont.split("\n")):
            for c, char in enumerate(line):
                if char == "E":
                    # "E" = "Entrée" : starting point
                    grid_values[c, l] = ("M", self.MacGyver_img)
                    init_position = (c, l)
                elif char == "S":
                    # "S" = "Sortie" : guardian's place
                    grid_values[c, l] = (char, self.Gardian_img)
                elif char == "x":
                    # wall
                    grid_values[c, l] = (char, self.wall_img)
                elif char == "o":
                    # floor
                    grid_values[c, l] = (char, self.floor_img)
                else:
                    print("Grille incorrecte")
                    return

        # Display labyrinth's structure
        #    This method is called at this stage so that additional elements will be displayed on top of the structure
        self.lab_screen.refresh_screen(grid_values)

        # Random definition of objects' position
        objects_to_find = []    # liste of objects to be found
        for elt in self.lab_data.object_list:
            # Random designation of an empty place (not wall not entrance or exit)
            special = choice([place for place in grid_values.keys() if grid_values[place][0] == "o"])
            object_name = elt + ".png"
            grid_values[special] = (elt, load_image(object_name, self.lab_data.ressources_path, self.lab_data.step))
            objects_to_find.append(elt)
            
        # Display objects at their defined position
        self.lab_screen.refresh_screen(grid_values)
        return init_position, objects_to_find, grid_values

    def move_char(self, current_pos, move_step_h, move_step_v):
        """ Characters' moves management """
        # Parameters en entrée : initial position and move step for each (horizontal and vertical) direction
        # All instructions are gathered in this single method and special moves (like diagonal) could be implemented as well

        destination_pos = (current_pos[0] + move_step_h, current_pos[1] + move_step_v)
        message_to_display = ""
        if self.grid_values[destination_pos][0] != "x":
            # If MacGyver meets the Guardian, check whether all objects have been found
            # If not, the game is lost and over
            if self.grid_values[destination_pos][0] == "S":
                if len(self.inventory) == 0:
                    self.lab_screen.display_msg("GAGNE ! Voulez-vous faire une nouvelle partie (O/N) ?")
                else:
                    self.lab_screen.display_msg("PERDU... Voulez-vous faire une nouvelle partie (O/N) ?")
                self.lab_end = True
                return current_pos
            
            # When MacGyver founds a new object, it's removed from the list
            if self.grid_values[destination_pos][0] in self.inventory:
                self.inventory.remove(self.grid_values[destination_pos][0])
                message_to_display = "Vous venez de trouver l'objet suivant : " + self.grid_values[destination_pos][0]

            # Change places' content after each move
            self.grid_values[destination_pos] = ("M", self.MacGyver_img)
            self.grid_values[current_pos] = ("o", self.floor_img)

            # Refresh display, incluiding a game message if any (object found, end of game)
            self.lab_screen.refresh_screen(self.grid_values, message_to_display)
            return destination_pos
        return current_pos