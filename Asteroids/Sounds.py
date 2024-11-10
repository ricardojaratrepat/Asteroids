# Import sound effects
import os
import sys
import pygame

def resource_path(relative_path):
    """ Obtiene la ruta absoluta del recurso, funciona para dev y PyInstaller """
    try:
        # PyInstaller guarda los archivos en una carpeta temporal
        base_path = sys._MEIPASS
    except AttributeError:
        # Durante el desarrollo, usamos la ruta actual
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
pygame.mixer.init()
# Carga de sonidos
snd_fire = pygame.mixer.Sound(resource_path("Sounds/fire.wav"))
snd_bangL = pygame.mixer.Sound(resource_path("Sounds/bangLarge.wav"))
snd_bangM = pygame.mixer.Sound(resource_path("Sounds/bangMedium.wav"))
snd_bangS = pygame.mixer.Sound(resource_path("Sounds/bangSmall.wav"))
snd_extra = pygame.mixer.Sound(resource_path("Sounds/extra.wav"))
snd_saucerB = pygame.mixer.Sound(resource_path("Sounds/saucerBig.wav"))
snd_saucerS = pygame.mixer.Sound(resource_path("Sounds/saucerSmall.wav"))
