import pygame
from grid import Grid
import block
import random
from block_spawner import block_manager

#TODO: Fix Rotation
#Fix block spawning
#Battle mechanical - Sending lines to each other or make thing go faster
#Lose game (block reach top)
#Sound effects

def Player1Input(block1):
    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_RIGHT:
            block1.move(1,0)
        if events.key == pygame.K_LEFT:
            block1.move(-1,0)
        if events.key == pygame.K_UP:
            block1.rotate(1)
        if events.key == pygame.K_DOWN:
            pygame.time.set_timer(TICK2, 50)
        

def Player2Input(block2):
    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_d:
            block2.move(1,0)
        if events.key == pygame.K_a:
            block2.move(-1,0)
        if events.key == pygame.K_w:
            block2.rotate(1)
        if events.key == pygame.K_s:
            pygame.time.set_timer(TICK1, 50)
pygame.init()
scene = pygame.display.set_mode((1024, 700))
scene.fill([0,0,0])

grid_height = 25
grid_width = 12

g1 = Grid(scene, grid_height, grid_width, 25,25, 64,650, [255,255,255], [0,0,0])
g2 = Grid(scene, grid_height, grid_width, 25, 25, 500, 650, [255,255,255], [0,0,0])

g1.setup()
g2.setup()

running = True
#Events
TICK1 = pygame.USEREVENT + 1
TICK2 = pygame.USEREVENT + 2

current_time = 200
pygame.time.set_timer(TICK1, current_time)
pygame.time.set_timer(TICK2, current_time)

block_manager1 = block_manager(g1)
block_manager2 = block_manager(g2)

block_manager1.spawn_block()
block_manager2.spawn_block()

line_due1 = False
line_due2 = False
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == TICK1:
            if(block_manager1.get_current_block().move(0,-1) == False):
                pygame.time.set_timer(TICK1, current_time)
                if(line_due1 == True):
                    g1.move_up()
                    line_due1 = False
                block_manager1.spawn_block()
                
                line_due2 = g1.clear_all_lines()
                
                
                for x in range(g1.get_width()):
                    if(g1.graphics_grid[x][g1.get_height()-1].block_present == True):
                        pygame.quit()
               
        if events.type == TICK2:
            if(block_manager2.get_current_block().move(0,-1) == False):
                pygame.time.set_timer(TICK2, current_time)
                
                if(line_due2 == True):
                    print('Line due for grid 2')
                    g2.move_up()
                    line_due2 = False

                block_manager2.spawn_block()
                line_due1 = g1.clear_all_lines()
                for x in range(g2.get_width()):
                    if(g2.graphics_grid[x][g2.get_height()-1].block_present == True):
                        pygame.quit()
                
        
        Player1Input(block_manager2.get_current_block())
        Player2Input(block_manager1.get_current_block())

        

    pygame.display.update()
    
