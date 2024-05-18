import pygame 
import math

import drawing

class Player():
    def __init__(self, x, y, speed, health, weapon, color, size, window):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.weapon = weapon
        self.color = color
        self.size = size
        self.window = window

        self.angle = 0
        
    def update(self, keys, mousePos):
        ### Movements
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        # To make the player not move through the screen
        if self.x < 0:
            self.x = 0
        elif self.x + self.size > self.window.get_width():
            self.x = self.window.get_width() - self.size
        if self.y < 0:
            self.y = 0
        elif self.y + self.size > self.window.get_height():
            self.y = self.window.get_height() - self.size
        #Rotation
        mouseX, mouseY = mousePos
        dx, dy = mouseX - self.x, mouseY - self.y
        self.angle = (math.atan2(dy, dx)) * 180 / math.pi
        
    def draw(self):
        drawing.playerDrawing(self.x, self.y, self.color, self.size, self.window)
        
        if self.weapon is not None:
            self.weapon.draw(self.window, self.x, self.y, self.size, self.angle)