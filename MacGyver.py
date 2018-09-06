"""Fichier principal de gestion du jeu de labyrinthe
Les principaux paramètres sopnt stockés dans le fichiers Donnees.py

POINTS A VOIR / A RESOUDRE
- ajuster l'affichage et les images à une fenêtre standard
- optimisation du code : remplacer les longues listes de "elif"
- Ajoputer des messages texte : Accueil du joueur, victoire ou défaite (+ aide ?)
- Gérer les exceptions
- Modulariser
- PEP8 / PEP20

"""

import pygame, os
from pygame.locals import *
from random import choice
from Donnees import *
from time import sleep

main_dir = os.path.split(os.path.abspath(__file__))[0] # Détection du répertoire courant

class Place:
    """Classe Emplacement pour gérer les positions dans la grille
    Sont concernés :
       - les infos d'espace libre ou de mur
       - l'emplacement des objets et des personnages

    Attributs : 
       - Position dans la grille
       - Nature de l'emplacement (contenu)

    Méthodes :
       - xoxoxoxo
    
    """

    def __init__(self, h_pos, v_pos, content):
        self.v_pos = v_pos      # Position verticale (ligne)
        self.h_pos = h_pos      # Position horizontale (colonne)
        self.content = content   # Contenu

    def __repr__(self):
        return "\nLigne {} / Colonne {} : contient {}".format(self.v_pos, self.h_pos, self.content)


class Lab_level:
    """ Classe destinée à gérer les niveaux de labyrinthe (ici un niveau unique)
    Sa définition s'appuie sur la grille trouvée dans les paramètres
    Principaux attributs : liste des emplacements de la grille
    Principales méthodes : initialisation de la gille
    """

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

class GameElements:
    """Classe des personnages et des objets disséminés dans le labyrinthe
    Gestion spécifique de leur position, et, concernant MacGyver, des mouvements et des objets récupérés """

    GameElements_list = [] # Liste des personnages créés

    def __init__(self, name, image, h_pos, v_pos, content):
        self.name = name            # A AJOUTER
        self.image = image
        self.pos = image.get_rect()
        self.objets = []
        self.position = Place(h_pos, v_pos, content)
        GameElements.GameElements_list.append(self)

    def __repr__(self):
        return "{} se trouve Ligne {} / Colonne {} !".format(self.name, self.position.v_pos, self.position.h_pos)

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
        if current_place.content in object_list and current_place.content not in self.objets:
            self.objets.append(current_place.content)
            print("{} a récupéré l'objet suivant : {}".format(self.name, current_place.content))
        
        if current_place.content == "S":
            if len(self.objets) == 3:
                print("GAGNE !")
                return
            else:
                print("PERDU !")
                return

def load_image(name):
    """ Chargement d'une image """
    image_name = os.path.join(main_dir, ressources_path, name)
    try:
        image = pygame.image.load(image_name)
    except pygame.error:
        print("### Impossible de charger l'image", name, "###")
        raise SystemExit
    image = pygame.transform.scale(image, (step, step))
    image = image.convert_alpha()  #Le convert() est-il bien nécessaire ???
    colorkey = image.get_at((1,1))
    image.set_colorkey((colorkey), RLEACCEL) 
    return image

def refresh_screen(screen, screen_structure, objects_to_display):
    """ Regroupement de toutes les commandes permettant l'affichage après chaque action """ 
    screen.fill(screen_structure)
    # La liste sera lue dans l'ordre inverse pour des raisons d'affichage et bliter dans l'ordre inverse de création des objets
    # OPTIMISATION A PREVOIR : intégrer tous les objets, sauf MacGyver, à l'arrière-plan
    for object in reversed(objects_to_display):
        object.pos.top = object.position.v_pos * step
        object.pos.left = object.position.h_pos * step
        screen.blit(object.image, object.pos)
    pygame.display.flip()   

def display_msg(screen, message):
    if pygame.font:
        font = pygame.font.Font(None, 40)
        text = font.render(message, 1, (150, 150, 150))
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
        screen.blit(text, textpos)    

def create_grid():
    """Création d'une liste des emplacements"""
    # Initialisation de la grille à partir du fichier
    grid_values = []
    f = open(grid_file, "r") # Ouverture du fichier
    cont = f.read() #lecture du fichier, contenu stocké dans une chaine
    l = 0
    for line in cont.split("\n"):
        c = 0
        for char in line:
            if char == "E": #Entrée : position initiale de MacGyver
                MacGyver = GameElements("MacGyver", load_image("MacGyver.png"), c, l, char)
            elif char == "S": #Sortie : position du gardien
                Guardian = GameElements("Le Gardien", load_image("Gardien.png"), c, l, char)
            elif char == "x": #Identification des murs
                mur = GameElements("Mur", load_image("temp_brick_wall.png"), c, l, char)
            grid_values.append(Place(c, l, char))
            c += 1
        l += 1

    # Positionnement aléatoire des objets
    for elt in object_list:
        # Définit un emplacement aléatoire parmi tous ceux qui n'ont aucun contenu (ni mur, ni personnage, ni objet)
        special = choice([place for place in grid_values if place.content == "o"])
        # Récupère l'élément de la liste des emplacements corrrespondant à la position définie aléatoirement
        special_place = get_place_from_pos(grid_values, special.v_pos, special.h_pos)
        # Affecte le contenu de l'élément à l'emplacement
        special_place.content = elt
        
        # Création d'un Object pour en gérer l'affichage
        object_name = elt + ".png"
        new_object = GameElements(elt, load_image(object_name), special.h_pos, special.v_pos, elt)

    # Trier la liste pour l'ordre d'affichage des différents éléments

    return grid_values, MacGyver, Guardian

def get_place_from_pos(places_list, v_pos, h_pos):
    """ Récupère un emplacement à partir de sa position
    L'objectif est d'identifier puis, éventuellement, de modifier le contenu d'un emplacement précis """
    for place in places_list:
        if place.h_pos == h_pos and place.v_pos == v_pos:
            return place

def main():
    """Instructions principales"""
    print("Initialisation du programme")
    pygame.init()

    screen_structure = 0, 0, 0 #structure du fond, noire pour commencer
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('MacGyver')

    lab_grid, MacGyver, Guardian = create_grid()

    refresh_screen(screen, screen_structure, GameElements.GameElements_list)

    display_msg(screen, "C'est parti !")

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                MacGyver.move_h(lab_grid, 1, screen_size)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                MacGyver.move_h(lab_grid, -1, screen_size)
            elif event.type == KEYDOWN and event.key == K_DOWN:
                MacGyver.move_v(lab_grid, 1, screen_size)
            elif event.type == KEYDOWN and event.key == K_UP:
                MacGyver.move_v(lab_grid, -1, screen_size)

        refresh_screen(screen, screen_structure, GameElements.GameElements_list)
        

if __name__ == "__main__":
    main()