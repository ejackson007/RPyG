import pygame
from pygame.locals import *

def draw_block():
    surface.fill((110,110,5))
    surface.blit(block,(block_x, block_y))
    #update screen
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500,500))
    #set background to white
    surface.fill((110,110,5))

    block = pygame.image.load("resources/block.jpg").convert()
    block_x = 100
    block_y = 100
    surface.blit(block,(block_x, block_y))
    #update screen
    pygame.display.flip()
    #event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running == False
                elif event.key == K_RIGHT:
                    block_x = block_x+20
                    draw_block()
                elif event.key == K_LEFT:
                    block_x = block_x-20
                    draw_block()
                elif event.key == K_UP:
                    block_y = block_y-20
                    draw_block()
                elif event.key == K_DOWN:
                    block_y = block_y+20
                    draw_block()
            elif event.type == QUIT:
                running = False