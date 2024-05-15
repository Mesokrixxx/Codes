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
        self.timer += 1 / 60
        
        if self.target == None:
            enemyPos = entity
        else:
            enemyPos = [self.target]

        for enemy in enemyPos:
            if enemy.faction != self.faction:
                dx, dy = enemy.x - self.x, enemy.y - self.y
                distance = math.sqrt(dx ** 2 + dy ** 2)

                if distance > (enemy.size / 1.2):
                    dx, dy = dx / distance, dy / distance
                    self.x += dx * self.speed
                    self.y += dy * self.speed
                    self.target = enemy
                    break
                else: 
                    if self.timer > self.damageCooldown:
                        attack(self.target, self.damage)
                        self.timer = 0
    
    def draw(self):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        
#Function
def attack(target, damage):
    if target!= None and target.health > 0:
        target.health -= damage

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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            chosenFaction = random.randint(0,2)
            entity.append(Entity(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], entityColor[str(chosenFaction)], entitySize, entitySpeed, entityFaction[chosenFaction], entityHealth, entityDamage, entityDamageCooldown))
    
    worldUpdate()
    worldRender()
    
    pygame.display.flip()
    fps.tick(60)

pygame.quit()

