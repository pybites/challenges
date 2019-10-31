# GUI with Python
# author: rsersh-py on PyBites - Rachel Hunt
import sys
import pygame
from pygame.locals import *

def main():

    pygame.init()

    pygame.display.set_caption("Click on the flower for a message in the shell window!")
    size = (675, 800)
    screen = pygame.display.set_mode(size)
    flower = pygame.image.load("blue-flower.png").convert()
    x = 135;
    y = 120;
    screen.blit(flower, ( x,y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if flower.get_rect().collidepoint(x,y):
                    print("Visit in person at the \nSan Francisco Botanical Gardens\n1199 9th Avenue")

if __name__ == '__main__':
    main()
