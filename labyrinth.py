# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
from random import randint, choice
from observers import *
from screen import *


class Labyrinth(Observer):
    """ Classe destinée à gérer les niveaux de labyrinthe (ici un niveau unique)
    Sa définition s'appuie sur la grille trouvée dans les paramètres
    Principaux attributs : liste des emplacements de la grille
    Principales méthodes : initialisation de la gille
    """

    def __init__(self, size_of_screen, grid_definition_file, object_list, ressources_path, step):
        Observer.__init__(self)
        self.grid_source_file = grid_definition_file
        self.lab_screen = Screen(size_of_screen, step)
        self.init_position, self.inventory, self.grid_values = self.def_grid_values(object_list, ressources_path, step)
        # self.lab_characters, self.lab_objects = self.init_display()
        # self.lab_display_list = self.lab_objects + [char for char in self.lab_characters.values()]
        # Initialisation de la surveillance des déplacements
        self.observe("Objet trouvé", self.update_display)

        self.MacGyver_img = load_image("MacGyver.png", ressources_path, step)
        # self.Gardian_img = load_image("Gardien.png", ressources_path, step)
        self.floor_img = load_image("temp_floor_tiles.png", ressources_path, step)
        # self.wall_img = load_image("temp_brick_wall.png", ressources_path, step)
    
    def def_grid_values(self, object_list, ressources_path, step):
        """Initialisation de la grille : attribution des valeurs aux emplacements"""
        # Attention : on n'utilise pas une propriété car on a besoin ensuite de modifier la grille

        # Récupération de la structure du labyrinthe du fichier txt
        init_position = ()
        grid_values = {}
        f = open(self.grid_source_file, "r") # Ouverture du fichier
        cont = f.read() #lecture du fichier, contenu stocké dans une chaine
        l = 0
        for line in cont.split("\n"):
            c = 0
            for char in line:
                if char == "E":
                    grid_values[c, l] = ("M", load_image("MacGyver.png", ressources_path, step))
                    init_position = (c, l)
                elif char == "S":
                    grid_values[c, l] = (char, load_image("Gardien.png", ressources_path, step))
                elif char == "x":
                    grid_values[c, l] = (char, load_image("temp_brick_wall.png", ressources_path, step))
                elif char == "o":
                    grid_values[c, l] = (char, load_image("temp_floor_tiles.png", ressources_path, step))
                else:
                    print("Grille incorrecte")
                    return
                c += 1
            l += 1
        # print(grid_values)
        # print("Grille Init OK")
        self.lab_screen.init_display(grid_values)

        # Positionnement aléatoire des objets sur le labyrinthe
        objects_to_find = []
        grid_objects = {}
        for elt in object_list:
            # print(elt)
            special = choice([place for place in grid_values.keys() if grid_values[place][0] == "o"])
            """ empty_places = []
            for key, value in grid_values.items():
                if value[0] == "o":
                    empty_places.append(key)
            special = choice(empty_places) """
            object_name = elt + ".png"
            grid_values[special] = (elt, load_image(object_name, ressources_path, step))
            grid_objects[special] = (elt, load_image(object_name, ressources_path, step))
            objects_to_find.append(elt)
            

        # print(grid_values)
        # print("Grille OK")
        self.lab_screen.refresh_screen(grid_objects)
        return init_position, objects_to_find, grid_values

    def update_display(self, elt_found):
        """ Supprime de la liste des objets à afficher celui qui vient d'être trouvé """
        self.lab_display_list = [elt for elt in self.lab_objects if elt.position.content != elt_found] + [char for char in self.lab_characters.values()]
        self.lab_screen.refresh_screen(self.lab_display_list)
        # print("Déplacement détecté")

    def move_char(self, current_pos, move_step_h, move_step_v):
        """ Déplacement des personnages """
        # print("Position actuelle :", current_pos, " / Déplacement prévu : ", move_step_h, "-", move_step_v)
        destination_pos = (current_pos[0] + move_step_h, current_pos[1] + move_step_v)
        # print("Destination :", self.grid_values[destination_pos][0])
        if self.grid_values[destination_pos][0] != "x":
            if self.grid_values[destination_pos][0] == "S":
                if len(self.inventory) == 0:
                    print("GAGNE !")
                else:
                    print("PERDU !")
                return current_pos
            if self.grid_values[destination_pos][0] in self.inventory:
                self.inventory.remove(self.grid_values[destination_pos][0])
            self.grid_values[destination_pos] = ("M", self.MacGyver_img)
            self.grid_values[current_pos] = ("o", self.floor_img)
            return destination_pos
        else:
            return current_pos

