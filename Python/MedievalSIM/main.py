import pygame
import math

#Variable
WindowPARAM = {"width": 800, "height": 800}
entity = []
entitySize = 16
entityColor = {"blue": (0, 0, 255), "green": (0, 255, 0), "red": (255, 0, 0)}
entityFaction = ["blue", "green", "red]
entitySpeed = 5

#Pygame init
pygame.init()
window = pygame.display.set_mode((WindowPARAM["width"], WindowPARAM["height"]))
fps = pygame.time.Clock()

#Class
class Entity():
    def __init__(self, x, y, color, size, speed, faction):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        self.faction = faction
    
    def movement(self):
        mousePos = pygame.mouse.get_pos()
        dx, dy = mousePos[0] - self.x, mousePos[1] - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        if distance > 0:
            dx, dy = dx / distance, dy / distance
            self.x += dx * self.speed
            self.y += dy * self.speed
    
    def draw(self):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

#Function
def worldRender():
    window.fill((255, 255, 255))
    
    for ety in entity:
        ety.draw()

def worldUpdate():
    for ety in entity:
        ety.movement()

#Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            entity.append(Entity(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], entityColor, entitySize, entitySpeed))
    
    worldUpdate()
    worldRender()
    
    pygame.display.flip()
    fps.tick(60)

pygame.quit()

