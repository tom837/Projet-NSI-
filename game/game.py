import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

pygame.display.set_caption("game")

a = True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
    screen.fill((159,231,82))
    pygame.display.update()