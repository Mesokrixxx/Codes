import pygame
import math
import random

#Variable
WindowPARAM = {"width": 800, "height": 800}
entity = []
entitySize = 16
entityColor = {"0": (0, 0, 255), "1": (0, 255, 0), "2": (255, 0, 0)}
entityFaction = ["blue", "green", "red"]
entitySpeed = 2
entityDamage = 1
entityDamageCooldown = 0.5 #Seconds
entityHealth = 4

#Pygame init
pygame.init()
window = pygame.display.set_mode((WindowPARAM["width"], WindowPARAM["height"]))
fps = pygame.time.Clock()

#Class
class Entity():
    def __init__(self, x, y, color, size, speed, faction, health, damage, damageCooldown):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        self.faction = faction
        self.health = health
        self.damage = damage
        self.damageCooldown = damageCooldown
        
        self.timer = 0
        self.target = None
    
    def update(self):
        #Collision
        if entity != []:
            for other_entity in entity:
                if other_entity != self and other_entity.health > 0:
                    dx, dy = other_entity.x - self.x, other_entity.y - self.y
                    distance = math.sqrt(dx ** 2 + dy ** 2)
                    if distance <= (self.size + other_entity.size) / 1.8:
                        dx = dx / distance
                        dy = dy / distance
                        self.x -= dx * self.speed
                        self.y -= dy * self.speed
                        #Atack
                        if self.timer >= self.damageCooldown and self.target is not None and self.target.health > 0:
                            self.target.health -= self.damage
                            self.timer = 0
                        else:
                            self.timer += 1 / 30 
        # Target part
        if self.target is None:
            closest_distance = float('inf')
            for other_entity in entity:
                if other_entity != self and other_entity.faction != self.faction and other_entity.health > 0:
                    distance = math.sqrt((other_entity.x - self.x) ** 2 + (other_entity.y - self.y) ** 2)
                    if distance < closest_distance:
                        closest_distance = distance
                        self.target = other_entity         
        else:
            if self.target.health <= 0:
                self.target = None
            else:
                dx, dy = self.target.x - self.x, self.target.y - self.y
                distance = math.sqrt(dx ** 2 + dy ** 2)
                if distance > (self.target.size / 1.5):
                    dx = dx / distance
                    dy = dy / distance
                    self.x += dx * self.speed
                    self.y += dy * self.speed
        
    def draw(self):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))


#Main loop
def worldRender():
    window.fill((255, 255, 255))
    
    for ety in entity:
        ety.draw()

def worldUpdate():
    for ety in entity:
        if ety.health <= 0:
            entity.remove(ety)
        ety.update()

running = True
paused = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            chosenFaction = random.randint(0,2)
            entity.append(Entity(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], entityColor[str(chosenFaction)], entitySize, entitySpeed, entityFaction[chosenFaction], entityHealth, entityDamage, entityDamageCooldown))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if paused: paused = False
            else: paused = True
        
    if not paused:   
        worldUpdate()
    worldRender()
    
    pygame.display.flip()
    fps.tick(60)

pygame.quit()

