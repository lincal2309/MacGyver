# -*-coding:Utf-8 -*

""" Gestion des éléments du jeu : objets et personnages 
La classe GameElements définit les attributs et méthodes de base : position et affichage
La classe fille Persons ajoute les attributs et méthodes spécifiques aux personnages : inventaire et déplacements
"""

import pygame
from pygame.locals import *
from places import *


class GameElements:
    """Classe des personnages et des objets disséminés dans le labyrinthe
    Gestion spécifique de leur position, et, concernant MacGyver, des mouvements et des objets récupérés """

    GameElements_list = [] # Liste des personnages créés

    def __init__(self, image, h_pos, v_pos, content):
        self.image = image
        self.pos = image.get_rect()
        self.position = Place(h_pos, v_pos, content)
        GameElements.GameElements_list.append(self)

    def __repr__(self):
        return "{} se trouve Ligne {} / Colonne {} !".format(self.name, self.position.v_pos, self.position.h_pos)


class Characters(GameElements):
    """ Classe fille de GameElements spécifique aux personnages : gestion de l'inventaire et des déplacements """

    def __init__(self, name, image, h_pos, v_pos, content, l_objects):
        GameElements.__init__(self, image, h_pos, v_pos, content)
        self.name = name
        self.objects = l_objects
        self.inventory = []

    def move_h(self, grid_values, move_step, screen_size):
        """ Déplacement horizontal des personnages """
        destination = get_place_from_pos(grid_values, self.position.v_pos, self.position.h_pos + move_step)
        if destination.content != "x":
            self.position.h_pos += move_step
            self.new_place(grid_values)
        
    def move_v(self, grid_values, move_step, screen_size):
        """ Déplacement vertical des personnages """
        destination = get_place_from_pos(grid_values, self.position.v_pos + move_step, self.position.h_pos)
        if destination.content != "x":
            self.position.v_pos += move_step
            self.new_place(grid_values)

    def new_place(self, grid_values):
        """ Actions liées à la position atteinte """
        current_place = get_place_from_pos(grid_values, self.position.v_pos, self.position.h_pos)
        if current_place.content in self.objects and current_place.content not in self.inventory:
            self.inventory.append(current_place.content)
            print("{} a récupéré l'objet suivant : {}".format(self.name, current_place.content))
        
        if current_place.content == "S":
            if len(self.inventory) == 3:
                print("GAGNE !")
                return
            else:
                print("PERDU !")
                return

        # refresh_screen(screen, screen_structure, GameElements.GameElements_list)



