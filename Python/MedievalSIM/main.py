import pygame

#Variable
WindowPARAM = {"width": 800, "height": 800}

#Pygame init
pygame.init()
window = pygame.display.set_mode((WindowPARAM["width"], WindowPARAM["height"]))
fps = pygame.time.Clock()

#Class


#Function


#Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    pygame.display.flip()
    fps.tick(60)

pygame.quit()

