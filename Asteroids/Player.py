# Create class for shattered ship
import math
import random
import pygame
from constants import gameDisplay, white, player_max_speed, fd_fric, bd_fric, display_width, display_height, player_size

class deadPlayer:
    def __init__(self, x, y, l):
        self.angle = random.randrange(0, 360) * math.pi / 180
        self.dir = random.randrange(0, 360) * math.pi / 180
        self.rtspd = random.uniform(-0.25, 0.25)
        self.x = x
        self.y = y
        self.lenght = l
        self.speed = random.randint(2, 8)

    def updateDeadPlayer(self):
        pygame.draw.line(gameDisplay, white,
                         (self.x + self.lenght * math.cos(self.angle) / 2,
                          self.y + self.lenght * math.sin(self.angle) / 2),
                         (self.x - self.lenght * math.cos(self.angle) / 2,
                          self.y - self.lenght * math.sin(self.angle) / 2))
        self.angle += self.rtspd
        self.x += self.speed * math.cos(self.dir)
        self.y += self.speed * math.sin(self.dir)


# Class player
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hspeed = 0
        self.vspeed = 0
        self.dir = -90
        self.rtspd = 0
        self.thrust = False
        self.infinite_ammo = False
        self.ammo_timer = 0
        self.invulnerable = False
        self.inv_timer = 0

    def updatePlayer(self):
        # Move player
        if self.infinite_ammo:
            if self.ammo_timer > 0:
                self.ammo_timer -= 1
            else:
                self.infinite_ammo = False
        if self.invulnerable:
            if self.inv_timer > 0:
                self.inv_timer -= 1
            else:
                self.invulnerable = False
        speed = math.sqrt(self.hspeed**2 + self.vspeed**2)
        if self.thrust:
            if speed + fd_fric < player_max_speed:
                self.hspeed += fd_fric * math.cos(self.dir * math.pi / 180)
                self.vspeed += fd_fric * math.sin(self.dir * math.pi / 180)
            else:
                self.hspeed = player_max_speed * math.cos(self.dir * math.pi / 180)
                self.vspeed = player_max_speed * math.sin(self.dir * math.pi / 180)
        else:
            if speed - bd_fric > 0:
                change_in_hspeed = (bd_fric * math.cos(self.vspeed / self.hspeed))
                change_in_vspeed = (bd_fric * math.sin(self.vspeed / self.hspeed))
                if self.hspeed != 0:
                    if change_in_hspeed / abs(change_in_hspeed) == self.hspeed / abs(self.hspeed):
                        self.hspeed -= change_in_hspeed
                    else:
                        self.hspeed += change_in_hspeed
                if self.vspeed != 0:
                    if change_in_vspeed / abs(change_in_vspeed) == self.vspeed / abs(self.vspeed):
                        self.vspeed -= change_in_vspeed
                    else:
                        self.vspeed += change_in_vspeed
            else:
                self.hspeed = 0
                self.vspeed = 0
        self.x += self.hspeed
        self.y += self.vspeed

        # Check for wrapping
        if self.x > display_width:
            self.x = 0
        elif self.x < 0:
            self.x = display_width
        elif self.y > display_height:
            self.y = 0
        elif self.y < 0:
            self.y = display_height

        # Rotate player
        self.dir += self.rtspd

    def drawPlayer(self):
        a = math.radians(self.dir)
        x = self.x
        y = self.y
        s = player_size
        t = self.thrust
        # Determinar el color
        color = (0, 0, 255) if self.invulnerable else white
        # Dibujar el jugador con el color correspondiente
        pygame.draw.line(gameDisplay, color,
                        (x - (s * math.sqrt(130) / 12) * math.cos(math.atan(7 / 9) + a),
                        y - (s * math.sqrt(130) / 12) * math.sin(math.atan(7 / 9) + a)),
                        (x + s * math.cos(a), y + s * math.sin(a)))

        pygame.draw.line(gameDisplay, color,
                        (x - (s * math.sqrt(130) / 12) * math.cos(math.atan(7 / 9) - a),
                        y + (s * math.sqrt(130) / 12) * math.sin(math.atan(7 / 9) - a)),
                        (x + s * math.cos(a), y + s * math.sin(a)))

        pygame.draw.line(gameDisplay, color,
                        (x - (s * math.sqrt(2) / 2) * math.cos(a + math.pi / 4),
                        y - (s * math.sqrt(2) / 2) * math.sin(a + math.pi / 4)),
                        (x - (s * math.sqrt(2) / 2) * math.cos(-a + math.pi / 4),
                        y + (s * math.sqrt(2) / 2) * math.sin(-a + math.pi / 4)))
        if t:
            pygame.draw.line(gameDisplay, color,
                            (x - s * math.cos(a),
                            y - s * math.sin(a)),
                            (x - (s * math.sqrt(5) / 4) * math.cos(a + math.pi / 6),
                            y - (s * math.sqrt(5) / 4) * math.sin(a + math.pi / 6)))
            pygame.draw.line(gameDisplay, color,
                            (x - s * math.cos(-a),
                            y + s * math.sin(-a)),
                            (x - (s * math.sqrt(5) / 4) * math.cos(-a + math.pi / 6),
                            y + (s * math.sqrt(5) / 4) * math.sin(-a + math.pi / 6)))


    def killPlayer(self):
        # Reset the player
        self.x = display_width / 2
        self.y = display_height / 2
        self.thrust = False
        self.dir = -90
        self.hspeed = 0
        self.vspeed = 0

