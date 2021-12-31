import pygame
from pygame.locals import *

def move_snake(x, y):
    surface.blit(bg, (0,0))
    '''snake works mostly in the way of follow the leader. This can be implemented by
    simply adding on one in the front and deleting the one in the back since each piece
    of the same size'''
    print(snake[-1])
    snake.append([snake[-1][0] + x, snake[-1][1] + y])
    print(snake)
    del(snake[0])
    print(snake)
    for rib in snake:
        surface.blit(block, (rib[0], rib[1]))

def add_rib():
    '''adds a rib to the snake. This is done by appending it to the front of the list, which 
    is the back of the snake. The side is determined by the relationship of the first 2 locations in the list.
    This is done so that the movement of the snake still feels natural. '''
    move_x = snake[0][0] - snake[1][0]
    move_y = snake[0][1] - snake[1][1]
    print(f"adding {move_x} {move_y}")
    nrib = [snake[0][0] + move_x, snake[0][1] + move_y]
    snake.insert(0, nrib)
    print(snake)
    for rib in snake:
        surface.blit(block, (rib[0], rib[1]))


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((400,400))
    #set background to white
    surface.fill((110,110,5))

    bg = pygame.image.load("resources/background.jpg").convert()
    surface.blit(bg, (0,0))

    block = pygame.image.load("resources/block.jpg").convert()
    #list that stores where the snake is
    snake = [[0,0], [0,40]]
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
                    move_snake(40,0)
                elif event.key == K_LEFT:
                    move_snake(-40,0)
                elif event.key == K_UP:
                    move_snake(0, -40)
                elif event.key == K_DOWN:
                    move_snake(0, 40)
                elif event.key == K_SPACE:
                    add_rib()
            elif event.type == QUIT:
                running = False
            pygame.display.flip()