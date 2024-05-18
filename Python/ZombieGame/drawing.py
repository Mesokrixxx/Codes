import pygame

def playerDrawing(x, y, color, size, window):
    pygame.draw.circle(window, (0, 0, 0), (x, y), size / 1.5)
    pygame.draw.circle(window, color, (x, y), size / 2)

def glockDrawing(window, x, y, width, height, angle):
    rect = pygame.Rect(x, y, width, height)
    surf = pygame.Surface(rect.size)
    pygame.draw.rect(surf, (42, 42, 42), rect)
    surf = pygame.transform.rotate(surf, angle)
    
    window.blit(surf, (x, y))