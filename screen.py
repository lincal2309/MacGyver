# -*-coding:Utf-8 -*

""" Display management for MacGyver.py game

    - Screen class is dedicated to graphical and moves management
    - load_image function is built to load images used in the game

"""

import pygame
import os
from pygame.locals import RLEACCEL

main_dir = os.path.split(os.path.abspath(__file__))[0] # Détection du répertoire courant


class Screen:
    """ Screen management class : 
        - Window's display
        - Moves management
        - Messages sent to the user
    """

    def __init__(self, screen_info):
        self.screen_structure = 0, 0, 0 #structure du fond, noire pour commencer
        self.screen = pygame.display.set_mode(screen_info.display_size)
        self.scale_ratio = screen_info.step
        self.scale = screen_info.scale
        pygame.display.set_caption('MacGyver')
        self.text_zone = pygame.Rect(0, screen_info.display_height - screen_info.step, screen_info.display_width, screen_info.step)

    def refresh_screen(self, objects_to_display, msg=""):
        """ Display update after each action
            May display a message in the dedicated zone if on is passed  """ 
        
        # Display messages is included for synchronisation purposes with character's moves

        # Text zone is refreshed to remove a previous message and / or clean the zone for a new one
        self.screen.fill(self.screen_structure, self.text_zone)

        # Grid potentially changed after last action => refresh display accordingly
        for position, object in objects_to_display.items():
            image_pos = (position[0] * self.scale_ratio, position[1] * self.scale_ratio)
            self.screen.blit(object[1], image_pos)
        
        # If requested, message sent to user
        if msg != "":
            self.display_msg(msg)
        
        pygame.display.flip()

    def display_msg(self, message, *messages):
        """ Diplay messages for the user """

        # Check if Fopnt module has been correctly charged (avoid to get an error if not)
        if pygame.font:
            self.screen.fill(self.screen_structure, self.text_zone)
            # Base font size 20 scaled by screen ratio calculated
            #    according to the actual user's screen
            font = pygame.font.Font(None, round(20 * self.scale))
            text = font.render(message, 1, (220, 0, 0))
            text_y = self.text_zone.y + self.text_zone.height / 2
            textpos = text.get_rect(centerx=self.text_zone.width / 2, centery=text_y)
            self.screen.blit(text, textpos)

            # Update method is used to refresh only the text zone
            pygame.display.update(self.text_zone)


def load_image(name, file_path, scale_ratio, alpha="True"):
    """ Load game's pictures """
    image_name = os.path.join(main_dir, file_path, name)

    # Check if the picture's file exists
    try:
        image = pygame.image.load(image_name)
    except pygame.error:
        print("### Impossible de charger l'image", name, "###")
        raise SystemExit
    image = pygame.transform.scale(image, (scale_ratio, scale_ratio))
    image = image.convert()

    # Depending on this parameter, transparency will be managed or not
    if alpha:
        colorkey = image.get_at((0,0))
        image.set_colorkey((colorkey), RLEACCEL) 
    return image
