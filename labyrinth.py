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

    def __init__(self, lab_data):
        Observer.__init__(self)
        self.lab_data = lab_data
        self.lab_end = False
        self.lab_screen = Screen(self.lab_data)

        # Chargement initial des images (évite des chargements multiples dans la première occurrence de la boucle)
        self.MacGyver_img = load_image(self.lab_data.MacGyver_file, self.lab_data.ressources_path, self.lab_data.step)
        self.Gardian_img = load_image(self.lab_data.Gardian_file, self.lab_data.ressources_path, self.lab_data.step)
        self.floor_img = load_image(self.lab_data.floor_file, self.lab_data.ressources_path, self.lab_data.step, False)
        self.wall_img = load_image(self.lab_data.wall_file, self.lab_data.ressources_path, self.lab_data.step)

        self.init_position, self.inventory, self.grid_values = self.def_grid_values(self.lab_data.object_list, self.lab_data.ressources_path, self.lab_data.step)
        # Initialisation de la surveillance des déplacements
        # self.observe("Objet trouvé", self.update_display)

    
    def def_grid_values(self, object_list, ressources_path, step):
        """Initialisation de la grille : attribution des valeurs aux emplacements"""
        # Attention : on n'utilise pas une propriété car on a besoin ensuite de modifier la grille

        # Récupération de la structure du labyrinthe du fichier txt
        init_position = ()
        grid_values = {}
        f = open(self.lab_data.grid_file, "r") # Ouverture du fichier
        cont = f.read() #lecture du fichier, contenu stocké dans une chaine
        l = 0
        for line in cont.split("\n"):
            c = 0
            for char in line:
                if char == "E":
                    grid_values[c, l] = ("M", self.MacGyver_img)
                    init_position = (c, l)
                elif char == "S":
                    grid_values[c, l] = (char, self.Gardian_img)
                elif char == "x":
                    grid_values[c, l] = (char, self.wall_img)
                elif char == "o":
                    grid_values[c, l] = (char, self.floor_img)
                else:
                    print("Grille incorrecte")
                    return
                c += 1
            l += 1

        # Affichage de la structure du labyrinthe
        self.lab_screen.init_display(grid_values)

        # Positionnement aléatoire des objets sur le labyrinthe
        objects_to_find = []
        for elt in self.lab_data.object_list:
            # print(elt)
            special = choice([place for place in grid_values.keys() if grid_values[place][0] == "o"])
            """ empty_places = []
            for key, value in grid_values.items():
                if value[0] == "o":
                    empty_places.append(key)
            special = choice(empty_places) """
            object_name = elt + ".png"
            grid_values[special] = (elt, load_image(object_name, self.lab_data.ressources_path, self.lab_data.step))
            objects_to_find.append(elt)
            
        # Affichage des objets par-dessus la structure
        self.lab_screen.refresh_screen(grid_values)
        return init_position, objects_to_find, grid_values

    def move_char(self, current_pos, move_step_h, move_step_v):
        """ Déplacement des personnages """
        # print("Position actuelle :", current_pos, " / Déplacement prévu : ", move_step_h, "-", move_step_v)
        destination_pos = (current_pos[0] + move_step_h, current_pos[1] + move_step_v)
        message_to_display = ""
        # print("Destination :", self.grid_values[destination_pos][0])
        if self.grid_values[destination_pos][0] != "x":
            if self.grid_values[destination_pos][0] == "S":
                if len(self.inventory) == 0:
                    print("GAGNE !")
                    self.lab_screen.display_msg("GAGNE ! Voulez-vous faire une nouvelle partie (O/N) ?")
                else:
                    print("PERDU !")
                    self.lab_screen.display_msg("PERDU... Voulez-vous faire une nouvelle partie (O/N) ?")
                self.lab_end = True
                return current_pos
            
            if self.grid_values[destination_pos][0] in self.inventory:
                self.inventory.remove(self.grid_values[destination_pos][0])
                message_to_display = "Vous venez de trouver l'objet suivant : " + self.grid_values[destination_pos][0]
            self.grid_values[destination_pos] = ("M", self.MacGyver_img)
            self.grid_values[current_pos] = ("o", self.floor_img)
            self.lab_screen.refresh_screen(self.grid_values, message_to_display)
            return destination_pos
        return current_pos

