# -*-coding:Utf-8 -*

""" Gestion de l'afichage dans le programme MacGyver.py

    - la classe screen gère tous les graphiques et mouvements
    - la fonction load_image est utilisée pour charger les images

"""

import pygame
import os
from pygame.locals import RLEACCEL

main_dir = os.path.split(os.path.abspath(__file__))[0] # Détection du répertoire courant


class Screen:
    """ Classe destinée à gérer l'affichage de la fenêtre, prendre en compte les mouvements et afficher les messages spéciaux """

    def __init__(self, screen_info):
        self.screen_structure = 0, 0, 0 #structure du fond, noire pour commencer
        self.screen = pygame.display.set_mode(screen_info.screen_size)
        self.scale_ratio = screen_info.step
        pygame.display.set_caption('MacGyver')
        self.text_zone = pygame.Rect(0, screen_info.screen_height - screen_info.step, screen_info.screen_width, screen_info.step)

    def init_display(self, objects_to_display):
        """ Regroupement de toutes les commandes permettant l'affichage après chaque action """ 
        self.screen.fill(self.screen_structure)
        for position, object in objects_to_display.items():
            image_pos = (position[0] * self.scale_ratio, position[1] * self.scale_ratio)
            self.screen.blit(object[1], image_pos)
        pygame.display.flip()

    def refresh_screen(self, objects_to_display, msg = ""):
        """ Regroupement de toutes les commandes permettant l'affichage après chaque action """ 
        # print("Refresh")
        self.screen.fill(self.screen_structure, self.text_zone)
        for position, object in objects_to_display.items():
            image_pos = (position[0] * self.scale_ratio, position[1] * self.scale_ratio)
            self.screen.blit(object[1], image_pos)
        if msg != "":
            self.display_msg(msg)
        pygame.display.flip()

    def display_msg(self, message, *messages):
        # print(message)
        if pygame.font:
            self.screen.fill(self.screen_structure, self.text_zone)
            font = pygame.font.Font(None, 30)
            text = font.render(message, 1, (220, 0, 0))
            text_y = self.text_zone.y + self.text_zone.height / 2
            textpos = text.get_rect(centerx=self.text_zone.width / 2, centery=text_y)
            self.screen.blit(text, textpos)
            pygame.display.update(self.text_zone)


def load_image(name, file_path, scale_ratio, alpha = "True"):
    """ Chargement d'une image """
    image_name = os.path.join(main_dir, file_path, name)
    try:
        image = pygame.image.load(image_name)
    except pygame.error:
        print("### Impossible de charger l'image", name, "###")
        raise SystemExit
    image = pygame.transform.scale(image, (scale_ratio, scale_ratio))
    image = image.convert()
    if alpha:
        colorkey = image.get_at((0,0))
        image.set_colorkey((colorkey), RLEACCEL) 
    return image
