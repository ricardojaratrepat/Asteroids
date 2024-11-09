import pygame
from constants import gameDisplay, player_size
from misc import isColliding
# Clase PowerUp
class PowerUp:
    def __init__(self, x, y, power_type):
        self.x = x
        self.y = y
        self.power_type = power_type  # 'ammo' o 'invulnerable'
        if self.power_type == 'ammo':
            self.color = (0, 255, 0)  # Verde para munición infinita
        elif self.power_type == 'invulnerable':
            self.color = (0, 0, 255)  # Azul para invulnerabilidad
        self.size = 10  # Tamaño del poder

    def updatePowerUp(self):
        # Dibujar el poder
        pygame.draw.circle(gameDisplay, self.color, (int(self.x), int(self.y)), self.size)

    def isCollected(self, player_x, player_y):
        # Verificar si el jugador ha recogido el poder
        return isColliding(self.x, self.y, player_x, player_y, self.size + player_size)

