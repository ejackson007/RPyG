import pygame
from pygame.locals import *
import pygame.freetype
import time
from random import randint
import os

def move_snake():
    surface.blit(bg, (0,40))
    surface.blit(fruit, (fx,fy))
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

def add_rib(score):
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

def fruitloc():
    '''Calculate random locations for the fruit. requirements are that its on the game board, and
    it has to be on a square that isn't already occupied by the snake'''
    works = False
    while not works:
        fx = (randint(0, 400) % 10) * 40
        fy = (randint(0, 400) % 10 + 1) * 40
        if [fx,fy] not in snake:
            works = True
    surface.blit(fruit, (fx,fy))
    return fx, fy

def out_of_bounds():
    if 0 > snake[-1][0] or snake[-1][0] >= 400:
        print(True)
        return True
    elif 40 > snake[-1][1] or snake[-1][1] >= 440:
        print(True)
        return True
    print(False)
    return False

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((400,440))
    #set background to white
    surface.fill((110,110,5))

    #get font and write Score at top
    score = 0
    fontpath = "/System/Library/Fonts/Geneva.ttf"
    pygame.freetype.init()
    fsize = 50
    myfont = pygame.freetype.Font(fontpath, fsize)
    myfont.render_to(surface, (0,0), f"Score: {score}", (0,0,0), None, size=50)

    bg = pygame.image.load("resources/background.jpg").convert()
    surface.blit(bg, (0,40))

    block = pygame.image.load("resources/block.jpg").convert()
    #list that stores each rib in the snake
    snake = [[0,40], [0,80], [0,120]]
    #default to moving down
    x = 0
    y = 40

    for rib in snake:
        surface.blit(block, (rib[0], rib[1]))
    
    #create fruit, and calculate random locations
    fruit = pygame.image.load("resources/apple.jpg").convert()
    fx, fy = fruitloc()
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
                    x = 40
                    y = 0
                elif event.key == K_LEFT:
                    x = -40
                    y = 0
                elif event.key == K_UP:
                    x = 0
                    y = -40
                elif event.key == K_DOWN:
                    x = 0
                    y = 40
                elif event.key == K_SPACE:
                    score += 1
                    myfont.render_to(surface, (0,0), f"Score: {score}", (0,0,0), None, size=50)
                    add_rib(score)
            elif event.type == QUIT:
                running = False
        time.sleep(.15)
        move_snake()
        #makes contact with fruit
        if [fx, fy] in snake:
            score += 1
            myfont.render_to(surface, (0,0), f"Score: {score}", (0,0,0), None, size=50)
            add_rib(score)
            fx, fy = fruitloc()

        #losing situation
        #duplicates means it crossed, or out of range
        if snake.index(snake[-1]) != (len(snake) - 1) or out_of_bounds():
            print("game over")
            running = False

        pygame.display.flip()