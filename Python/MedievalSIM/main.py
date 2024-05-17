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
    def __init__(self, x, y, color, size, speed, faction, health, damage, damageCooldown, range):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        self.faction = faction
        self.health = health
        self.damage = damage
        self.damageCooldown = damageCooldown
        self.range = range
        
        self.timer = 0
        self.target = None
    
    def update(self):
        #Collision
        if entity != []:
            for otherEntity in entity:
                if otherEntity != self and otherEntity.health > 0:
                    dx, dy = otherEntity.x - self.x, otherEntity.y - self.y
                    distance = math.sqrt(dx ** 2 + dy ** 2)
                    if distance <= (self.size + otherEntity.size) / 2:
                        if distance > 0:
                            dx = dx / distance
                            dy = dy / distance
                            self.x -= dx * self.speed
                            self.y -= dy * self.speed
                        else: 
                            self.x -= random.randint(-1, 1)
                            self.y -= random.randint(-1, 1) 
        # Target part
        if self.target is None:
            closestDistance = float('inf')
            for otherEntity in entity:
                if otherEntity != self and otherEntity.faction != self.faction and otherEntity.health > 0:
                    distance = math.sqrt((otherEntity.x - self.x) ** 2 + (otherEntity.y - self.y) ** 2)
                    if distance < closestDistance:
                        closestDistance = distance
                        self.target = otherEntity         
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
        # Attack
        if self.target is not None and self.target.health > 0:
            distance = math.sqrt((self.target.x - self.x) ** 2 + (self.target.y - self.y) ** 2)
            if distance <= self.range:
                if self.timer > self.damageCooldown:
                    self.target.health -= self.damage
                    self.timer = 0
                else:
                    self.timer += 1 / 60   
            
    def draw(self):
        pygame.draw.rect(window, (0, 0, 0), (self.x - 2, self.y - 2, self.size + 4, self.size + 4))
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))


#Main loop
def worldRender():
    window.fill((255, 255, 255))
    
    for entities in entity:
        entities.draw()

def worldUpdate():
    for entities in entity:
        if entities.health <= 0:
            entity.remove(entities)
        entities.update()

running = True
paused = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            chosenFaction = random.randint(0,2)
            spawnX = random.randint(0, WindowPARAM["width"] - entitySize)
            spawnY = random.randint(0, WindowPARAM["height"] - entitySize)
            for i in range(random.randint(1,10)):
                entity.append(Entity(spawnX, spawnY, entityColor[str(chosenFaction)], entitySize, entitySpeed, entityFaction[chosenFaction], entityHealth, entityDamage, entityDamageCooldown, entitySize * 1.2))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if paused: paused = False
            else: paused = True
        
    if not paused:   
        worldUpdate()
    worldRender()
    
    pygame.display.flip()
    fps.tick(60)

pygame.quit()

