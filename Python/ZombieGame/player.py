import pygame 

class Player():
    def __init__(self, x, y, speed, health, weapon, color, size, surface):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.weapon = weapon
        self.color = color
        self.size = size
        self.surface = surface

    def update(self, keys):
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
        elif self.x + self.size > self.surface.get_width():
            self.x = self.surface.get_width() - self.size

        if self.y < 0:
            self.y = 0
        elif self.y + self.size > self.surface.get_height():
            self.y = self.surface.get_height() - self.size
    
    def draw(self):
        pygame.draw.circle(self.surface, (0, 0, 0), (self.x, self.y), self.size / 1.5)
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.size / 2)