# -*-coding:Utf-8 -*

"""Fichier principal de gestion du jeu de labyrinthe
Les principaux paramètres sopnt stockés dans le fichiers Donnees.py

POINTS A VOIR / A RESOUDRE
- VARIABLES GLOBALES : import de Donnees.py UNIQUEMENT dans le programme principal ; passer les autres en paramètre des appels de classes
- ajuster l'affichage et les images à une fenêtre standard
- optimisation du code : remplacer les longues listes de "elif"
- Ajoputer des messages texte : Accueil du joueur, victoire ou défaite (+ aide ?)
- Gérer les exceptions
- PEP8 / PEP20

"""

import pygame, os
from pygame.locals import *
from random import choice
from Donnees import *
from places import *
from GameElements import *
from screen import *

class Labyrinth:
    """ Classe destinée à gérer les niveaux de labyrinthe (ici un niveau unique)
    Sa définition s'appuie sur la grille trouvée dans les paramètres
    Principaux attributs : liste des emplacements de la grille
    Principales méthodes : initialisation de la gille
    """

    def __init__(self, size_of_screen, grid_definition_file):
        self.grid_source_file = grid_definition_file
        self.lab_screen = Screen(size_of_screen)
        self.grid_values = self.def_grid_values()
        self.lab_characters, self.lab_objects = self.def_content()

    def def_grid_values(self):
        """Initialisation de la grille : attribution des valeurs aux emplacements"""
        # Attention : on n'utilise pas une propriété car on a besoin ensuite de modifier la grille
        grid_values = []
        f = open(self.grid_source_file, "r") # Ouverture du fichier
        cont = f.read() #lecture du fichier, contenu stocké dans une chaine
        l = 0
        for line in cont.split("\n"):
            c = 0
            for char in line:
                grid_values.append(Place(c, l, char))
                c += 1
            l += 1
        return grid_values

    def def_content(self):
        """ Initialisation du contenu : personnages et objets disséminés dans le labyrinthe"""
        char = {}
        obj = []
        for place in self.grid_values:
            if place.content == "E": #Entrée : position initiale de MacGyver
                char["MacGyver"] = Characters("MacGyver", load_image("MacGyver.png", ressources_path, step), place.h_pos, place.v_pos, place.content, object_list)
            elif place.content == "S": #Sortie : position du gardien
                char["Guardian"] = Characters("Le Gardien", load_image("Gardien.png", ressources_path, step), place.h_pos, place.v_pos, place.content, "")
            elif place.content == "x": #Identification des murs
                obj.append(GameElements(load_image("temp_brick_wall.png", ressources_path, step), place.h_pos, place.v_pos, place.content))

        for elt in object_list:
            # Définit un emplacement aléatoire parmi tous ceux qui n'ont aucun contenu (ni mur, ni personnage, ni objet)
            # Création d'une liste pour lister les emplacements libres
            special = choice([place for place in self.grid_values if place.content == "o"])
            # Affecte le contenu de l'élément à l'emplacement
            for index, place in enumerate(self.grid_values):
                if place.h_pos == special.h_pos and place.v_pos == special.v_pos:
                    self.grid_values[index].content = elt

            # Création d'un GameElement pour en gérer l'affichage
            # Seule l'instanciation compte car alimente la liste globale qui est utilisée pour l'affichage
            object_name = elt + ".png"
            new_object = GameElements(load_image(object_name, ressources_path, step), special.h_pos, special.v_pos, elt)

        return char, obj

def main():
    """Instructions principales"""
    pygame.init()

    lab_level = Labyrinth(screen_size, grid_file)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                lab_level.lab_characters["MacGyver"].move_h(lab_level.grid_values, 1, screen_size)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                lab_level.lab_characters["MacGyver"].move_h(lab_level.grid_values, -1, screen_size)
            elif event.type == KEYDOWN and event.key == K_DOWN:
                lab_level.lab_characters["MacGyver"].move_v(lab_level.grid_values, 1, screen_size)
            elif event.type == KEYDOWN and event.key == K_UP:
                lab_level.lab_characters["MacGyver"].move_v(lab_level.grid_values, -1, screen_size)

        lab_level.lab_screen.refresh_screen(GameElements.GameElements_list, step)
        

if __name__ == "__main__":
    main()