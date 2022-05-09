from tkinter import W
import pygame
import grid
import block
import random

def Player1Input():
    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_RIGHT:
            blocks2[-1].move(1,0)
        if events.key == pygame.K_LEFT:
            blocks2[-1].move(-1,0)
        if events.key == pygame.K_UP:
            blocks2[-1].rotate(1)
        if events.key == pygame.K_DOWN:
            pass
def Player2Input():
    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_d:
            blocks1[-1].move(1,0)
        if events.key == pygame.K_a:
            blocks1[-1].move(-1,0)
        if events.key == pygame.K_w:
            blocks1[-1].rotate(1)
        if events.key == pygame.K_s:
            pass
pygame.init()
scene = pygame.display.set_mode((1024, 700))
scene.fill([0,0,0])

grid_height = 25
grid_width = 12

g1 = grid.Grid(scene, grid_height, grid_width, 25,25, 64,650, [255,255,255], [0,0,0])
g2 = grid.Grid(scene, grid_height, grid_width, 25, 25, 500, 650, [255,255,255], [0,0,0])



g1.setup()
g2.setup()

running = True
#Events
TICK = pygame.USEREVENT + 1
pygame.time.set_timer(TICK, 150)


blocks1 = list()
blocks1.append(block.block(g1, "I"))
blocks2 = list()
blocks2.append(block.block(g2, "I"))
possible_letters = ["S", "J", "I", "O", "Z", "T", "L"]
i=0
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == TICK:
            if(blocks1[-1].move(0, -1) == False):
                blocks1.append(block.block(g1, possible_letters[random.randrange(0, len(possible_letters))]))
                del blocks1[-2]
                for i in range(g1.get_height()):
                    if(g1.check_line(i) == True):
                        g1.clear_line(i)
            if(blocks2[-1].move(0, -1) == False):
                blocks2.append(block.block(g2, possible_letters[random.randrange(0, len(possible_letters))]))
                del blocks2[-2]
                for i in range(g2.get_height()):
                    if(g2.check_line(i) == True):
                        g2.clear_line(i)
        Player1Input()
        Player2Input()

        

    pygame.display.update()
    
