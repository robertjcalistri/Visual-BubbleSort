import sys
import pygame
import random
from pygame.locals import *

BLACK = (0,0,0)
GREEN= (0,255,0)
RED = (255,0,0)

pygame.init()

clock = pygame.time.Clock()

class Block(object):
    
    def __init__(self, x, y, width, height, color):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = color

    def drawBlock(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

window_size = (800, 500)
display = pygame.display.set_mode(window_size)
pygame.display.set_caption("Visual Bubble Sorter")

list_heights = []
number_columns = 26

for i in range(number_columns):
    list_heights.append(random.randint(0,400))

print(list_heights)

def bubblesort(listOfHeights):
    for i in range(number_columns - 1):
        for j in range(number_columns - 1):
            if listOfHeights[i] > listOfHeights[i+1]:
                temp = listOfHeights[i]
                listOfHeights[i] = listOfHeights[i+1]
                listOfHeights[i+1] = temp
            
running = True
while running:
    
    display.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            running = False

    

    xpos = 10
    width = (790 - number_columns * xpos) / number_columns
    object_list = []
    for height in list_heights:
        B = Block(xpos,0,width,height,GREEN)
        B.drawBlock(display)
        object_list.append(B)
        xpos += 30

    bubblesort(list_heights)
    
    pygame.display.flip()
    clock.tick(10)
    
