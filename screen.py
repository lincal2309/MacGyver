# -*-coding:Utf-8 -*

""" Gestion de l'afichage dans le programme MacGyver.py

    - la classe screen gère tous les graphiques et mouvements
    - la fonction load_image est utilisée pour charger les images

"""

import pygame, os
from pygame.locals import RLEACCEL

main_dir = os.path.split(os.path.abspath(__file__))[0] # Détection du répertoire courant


class Screen:
    """ Classe destinée à gérer l'affichage de la fenêtre, prendre en compte les mouvements et afficher les messages spéciaux """

    def __init__(self, size_of_screen, scale_ratio):
        self.screen_structure = 0, 0, 0 #structure du fond, noire pour commencer
        self.screen = pygame.display.set_mode(size_of_screen)
        self.scale_ratio = scale_ratio
    #     self.screen_init = self.screen
    #     self.default_block = pygame.Rect(0, 0, scale_ratio, scale_ratio)
    #     self._list_objects_to_display = []
        pygame.display.set_caption('MacGyver')

    # @property
    # def display_list(self):
    #     display_list = []
    #     if self._list_objects_to_display != []:
    #         for object in self._list_objects_to_display:
    #             object.pos.top = object.position.v_pos * self.scale_ratio
    #             object.pos.left = object.position.h_pos * self.scale_ratio
    #             display_list.append(self.screen.blit(object.image, object.pos))
    #     return display_list
    
    def init_display(self, objects_to_display):
        """ Regroupement de toutes les commandes permettant l'affichage après chaque action """ 
        self.screen.fill(self.screen_structure)
        for position, object in objects_to_display.items():
            image_pos = (position[0] * self.scale_ratio, position[1] * self.scale_ratio)
            self.screen.blit(object[1], image_pos)
        pygame.display.flip()
        return self.screen

    def refresh_screen(self, objects_to_display):
        """ Regroupement de toutes les commandes permettant l'affichage après chaque action """ 
        # self.screen.fill(self.screen_structure)
        for position, object in objects_to_display.items():
            image_pos = (position[0] * self.scale_ratio, position[1] * self.scale_ratio)
            # object.pos.top = object.position.v_pos * self.scale_ratio
            # object.pos.left = object.position.h_pos * self.scale_ratio
            self.screen.blit(object[1], image_pos)
        pygame.display.flip()

    def display_msg(self, message):
        if pygame.font:
            font = pygame.font.Font(None, 40)
            text = font.render(message, 1, (150, 150, 150))
            textpos = text.get_rect(centerx=self.screen.get_width()/2, centery=self.screen.get_height()/2)
            self.screen.blit(text, textpos)


def load_image(name, file_path, scale_ratio):
    """ Chargement d'une image """
    image_name = os.path.join(main_dir, file_path, name)
    try:
        image = pygame.image.load(image_name)
    except pygame.error:
        print("### Impossible de charger l'image", name, "###")
        raise SystemExit
    image = pygame.transform.scale(image, (scale_ratio, scale_ratio))
    image = image.convert()
    colorkey = image.get_at((0,0))
    image.set_colorkey((colorkey), RLEACCEL) 
    return image
