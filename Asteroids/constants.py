

import pygame

pygame.font.init()

import os
import sys

def resource_path(relative_path):
    """ Obtiene la ruta absoluta del recurso, funciona para dev y PyInstaller """
    try:
        # PyInstaller guarda los archivos en una carpeta temporal
        base_path = sys._MEIPASS
    except AttributeError:
        # Durante el desarrollo, usamos la ruta actual
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Usar la ruta dinámica para cargar la fuente
font_path = resource_path("Font/Vectorb.ttf")
custom_font = pygame.font.Font(font_path, 35)


# Initialize constants
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

player_size = 10
fd_fric = 0.5
bd_fric = 0.1
player_max_speed = 20
player_max_rtspd = 10
bullet_speed = 15
saucer_speed = 5
small_saucer_accuracy = 10
