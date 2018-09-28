# -*-coding:Utf-8 -*

"""Fichier de données et paramètres du jeu de labyrinthe
   Données gérées sous forme d'une classe dédiée pour faciliter l'évolutivité 
   
   Classe créée avec un pattern Singleton dans la mesure où les paramètres ne sont utiles que sur une seul instance
   
   """

from observers import *

@singleton
class Donnees:
    """ Appel au décorateur Singletin du module observers pour s'assurer qu'une seule instance de la classe ne soit créée """

    def __init__(self):
        # Dimensions du labyrinthe et de la fenêtre
        self.lab_dim = 15
        self.step = 60 # A REVOIR - variable de pas pour gérer le déplacement - dépend de la taille de simages et de la grille
        self.screen_size = self.screen_width, self.screen_height = self.step * self.lab_dim, self.step * (self.lab_dim + 1)

        # Nom du fichier définissant grille
        self.grid_file = "grille.txt"

        # Objets à positionner dans la grilles
        self.object_list = ["Seringue", "Aiguille", "Ether"]

        # Dossier des images nécessaires au jeu
        self.ressources_path = ".\\Ressources\\"

        #Images du jeu
        self.MacGyver_file = "MacGyver.png"
        self.Gardian_file = "Gardien.png"
        self.floor_file = "temp_brick_wall.png"
        self.wall_file = "temp_floor_tiles.png"


def main():

    data = Donnees()
    print("Dimensions totales : ", data.screen_size)
    print("Hauteur : ", data.screen_height, " / Largeur : ", data.screen_width)

if __name__ == "__main__":
    main()

