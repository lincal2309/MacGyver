# -*-coding:Utf-8 -*

""" Gestion dees emplacements du programme MacGyver.py 

    - La classe Place définit tous les emplacements gérés dans le jeu
    - la fonction get_place_from_pos retourne une Place à partir de la position (pour en récupérer le contenu

"""

class Place:
    """ Classe Emplacement pour gérer les positions dans la grille

        Attributs : 
        - Position dans la grille
        - Nature de l'emplacement (contenu)

    """

    def __init__(self, h_pos, v_pos, content):
        self.v_pos = v_pos      # Position verticale (ligne)
        self.h_pos = h_pos      # Position horizontale (colonne)
        self.content = content   # Contenu

    def __repr__(self):
        return "\nLigne {} / Colonne {} : contient {}".format(self.v_pos, self.h_pos, self.content)


def get_place_from_pos(places_list, v_pos, h_pos):
    """ Récupère un emplacement à partir de sa position
        L'objectif est d'identifier puis, éventuellement, de modifier le contenu d'un emplacement précis """

    for place in places_list:
        if place.h_pos == h_pos and place.v_pos == v_pos:
            return place

