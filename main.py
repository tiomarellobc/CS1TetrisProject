import pygame
import grid

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
pygame.time.set_timer(TICK, 500)


while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == TICK:
            pass
    
    pygame.display.update()
    