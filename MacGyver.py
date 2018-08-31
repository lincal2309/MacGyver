"""Fichier principal de gestion du jeu de labyrinthe
Les principaux paramètres sopnt stockés dans le fichiers Donnees.py"""

from random import randrange
from Donnees import *


class Place:
    """Classe Emplacement pour gérer les positions dans la grille
    Sont concernés :
       - les infos d'espace libre ou de mur
       - l'emplacement des objets et des personnages

    Attributs : 
       - Position dans la grille
       - Nature de l'emplacement (contenu)

    Méthodes :
       - xoxoxoxo"""

    def __init__(self, v_pos, h_pos, content):
        self.v_pos = v_pos      # Position verticale (ligne)
        self.h_pos = h_pos      # Position horizontale (colonne)
        self.content = content   # Contenu

    def __repr__(self):
        return "Ligne {} / Colonne {} : contient {}\n".format(self.h_pos, self.v_pos, self.content)


class Lab_level:
    """ Classe destinée à gérer les niveaux de labyrinthe (ici un niveau unique)
    Sa définition s'appuie sur la grille trouvée dans les paramètres
    Principaux attributs : liste des emplacements de la grille
    Principales méthodes : initialisation de la gille"""

    def __init__(self):
        pass

    @property
    def list_places(self):
        places = []
        elt = ""
        for x in range(1, lab_dim):
            for y in range(1, lab_dim):
                place = [x, y, elt]
                places.append(place)
        return places



    def init_grid(self):
        """Initialisation de la grille : attribution des valeurs aux emplacements"""
        # Récupération des données de la grille, identification des emplacements
        # Création d'une liste pour lister les emplacements libres
        # Rechercher un éléments par défaut pour chaque objet et personnage à positionner
        # Suppression de l'emplacement retenu de la liste

class Person:
    """Classe des personnages : MacGyver et le gardien du labyrinthe
    Gestion spécifique de leur position, et, concernant MacGyver, des mouvdements et des objets récupérés """

    def __init__(self, name, v_pos, h_pos, content):
        self.name = name
        self._v_pos = v_pos
        self._h_pos = h_pos
        self._content = content

    @property
    def position(self):
        return Place(self._v_pos, self._h_pos, self._content)

    def __repr__(self):
        return "{} se trouve Ligne {} / Colonne {} !".format(self.name, self.position.h_pos, self.position.v_pos)


def create_grid(grid_file):
    """Création d'une liste des emplacements"""
    # Initialisation de la grille à partir du fichier
    grid_values = []
    f = open(grid_file, "r") # Ouverture du fichier
    cont = f.read() #lecture du fichier, contenu stocké dans une chaine
    l = lab_dim #la première ligne du fichier est la dernière de la grille si l'origine est dans l'angle inférieur gauche
    for line in cont.split("\n"):
        c = 0
        for char in line:
            c += 1
            if char == "E": #Entrée : position initiale de MacGyver
                McGyver = Person("MacGyver", c, l, char)
            elif char == "S": #Sortie : position du gardien
                Guardian = Person("Le Gardien", c, l, char)
            grid_values.append(Place(c, l, char))
        l -= 1
    
    # Positionnement aléatoire des objets
    spec_places = [] # Liste de contrôle pour vérifier que tous les objets sont pris en compte
    for elt in object_list:
        free_places = [place for place in grid_values if place.content == "o"]
        p = randrange(1, len(free_places))
        # A MODIFIER : utiliser la méthode random.CHOICE(free_places)
        special = free_places[p]
        # print("Object spécial : ", i, "Ligne ", special.v_pos, " / Colonne ", special.h_pos)
        spec_place = get_place_from_pos(grid_values, special.v_pos, special.h_pos)
        spec_place.content = elt
        spec_places.append(spec_place)

    return grid_values, McGyver, Guardian

def get_place_from_pos(places_list, v_pos, h_pos):
    """ Récupère un emplacement à partir de sa position
    L'objectif est de pouvoiridentifier pui, éventuellement, modifier le contenu d'un emplacement précis """
    for place in places_list:
        if place.h_pos == h_pos and place.v_pos == v_pos:
            return place

def main():
    """Instructions principales"""
    # Initialisation des variables globales
    # MGyver = Guardian = ""
    print("Initialisation du programme")
    # print(create_grid(grid_file))
    lab_grid, McGyver, Guardian = create_grid(grid_file)
    # print(McGyver)
    # print(Guardian)
    # print(lab_grid)

if __name__ == "__main__":
    main()