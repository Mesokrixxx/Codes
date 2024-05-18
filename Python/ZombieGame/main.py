import pygame

import player
import weapon

### Pygame Init
WindowPARAM = {"width": 800, "height": 800}
pygame.init()
window = pygame.display.set_mode((WindowPARAM["width"], WindowPARAM["height"]))
fps = pygame.time.Clock()

### Variables
glock = weapon.Weapon(0, 0, 0, 0, 0, 5, 12)
newPlayer = player.Player((WindowPARAM["width"] / 2), (WindowPARAM["height"] / 2), 4, 10, glock, (0, 0, 255), 20, window)

### Functions
def worldUpdate(keys, mousePos):
    newPlayer.update(keys, mousePos)

def worldRender():
    window.fill((128, 128, 128))
    
    newPlayer.draw()
    
### Main Loop
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if paused: paused = False
                else: paused = True
                
    keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    
    if not paused:
        worldUpdate(keys, mousePos)
    worldRender()
    
    pygame.display.flip()
    fps.tick(60)
    
pygame.quit()