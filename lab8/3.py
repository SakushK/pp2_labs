from math import sqrt
import pygame
from random import randint

pygame.init()

#Global Variables:
WIDTH, HEIGHT = 800, 600
FPS = 60

#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

#Initializing:
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

drawing = False

color = BLACK

#Functions for each drawing:
def drawRect(color, pos, width, height):  
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4) 

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

RAD = 30


screen.fill(WHITE)
#Starting and ending positions of rectangle while drawing:
start_pos = 0
end_pos = 0

#Change the mode:
mode = 0
# 0 - Rect
# 1 - Circle
# 2 - Eraser

#List that contains 20 random colors - change the color
all_colors = []

for _ in range(20):
    all_colors.append((randint(0,255), randint(0,255), randint(0,255)))


while not finished:

    pos = pygame.mouse.get_pos() #cursor position

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit from programm 
            finished = True
        
        #choose the color:
        if event.type == pygame.MOUSEBUTTONDOWN:#mouse button down
            drawing = True
            start_pos = pos #start of the stuck

            if pos[0] > 20 and pos[0] < 720 and pos[1] > 20 and pos[1] < 40: #color choosing
                color = screen.get_at(pos)
       
        if event.type == pygame.MOUSEBUTTONUP:#mouse button up
            drawing = False
            end_pos = pos# записываем конец нажатия мышки

            rect_x = abs(start_pos[0] - end_pos[0])#разница х
            rect_y = abs(start_pos[1] - end_pos[1])#разница у
            
            if mode == 0:                              #выбор режима
                drawRect(color, start_pos, rect_x, rect_y)
            elif mode == 1:
                drawCircle(color, start_pos, rect_x)
            

        if event.type == pygame.MOUSEMOTION and drawing:  #стерка 
            if mode == 2:
                eraser(pos, RAD)
        
        if event.type == pygame.KEYDOWN:               #при нажатий на space мы будем переходить на следующий мод
            if event.key == pygame.K_SPACE:             #и если на последнем моде мы нажмем на пробел, все перейдет на первый мод
                mode += 1
                if mode==7:mode=0
            if event.key == pygame.K_BACKSPACE:      #при нажатия на backspace, весь экран очищается
                screen.fill(WHITE)

    w = 30  # width of rectangles containing 20 colors
   
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * w, 20, w, 20)) #цвета
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
