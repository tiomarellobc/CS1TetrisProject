import pygame
from grid import Grid
from block_spawner import block_manager

def SecondPlayerInput(block):
    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_RIGHT:
            block.move(1,0)
        if events.key == pygame.K_LEFT:
            block.move(-1,0)
        if events.key == pygame.K_UP:
            block.rotate(1)
        if events.key == pygame.K_DOWN:
            pygame.time.set_timer(TICK2, 50)
        

def FirstPlayerInput(block):
    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_d:
            block.move(1,0)
        if events.key == pygame.K_a:
            block.move(-1,0)
        if events.key == pygame.K_w:
            block.rotate(1)
        if events.key == pygame.K_s:
            pygame.time.set_timer(TICK1, 50)

def display_tutorial(display):
    '''Displays the controls and tutorial'''
    tutorial = pygame.image.load('Assets/Tutorial.png')
    tutorial = pygame.transform.scale(tutorial, (900,700))
    display.blit(tutorial, (0,0))
    #tutorial_text = pygame.font.SysFont('Helvetica', 24)
    #tutorial = tutorial_text.render('Player 1 : W - Rotation, A/D - Move, S - Drop fast', True, (255,255,255))
    #tutorial2 = tutorial_text.render('Player 2 : (Arrow) Up - Rotation, Left/Right - Move,  Down - Drop Fast', True, (255,255,255))
    #tutorial3 = tutorial_text.render("Hit 'P' to Start", True, (255,255,255))
    #display.blit(tutorial, (150, 200))
    #display.blit(tutorial2, (100, 400))
    #display.blit(tutorial3, (350, 600))
    pygame.display.flip()
    tutorial_running = True
    while tutorial_running:
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_p:
                    tutorial_running = False
    display.fill((0,0,0))

pygame.init()
scene = pygame.display.set_mode((900, 700))
pygame.display.set_caption("B(attle)-Tetris")
scene.fill([0,0,0])

display_tutorial(scene)


running = True

grid_height = 25
grid_width = 12

g1 = Grid(scene, grid_height, grid_width, 25,25, 64,650, [255,255,255], [0,0,0])
g2 = Grid(scene, grid_height, grid_width, 25, 25, 500, 650, [255,255,255], [0,0,0])

g1.setup()
g2.setup()


#Events
TICK1 = pygame.USEREVENT + 1
TICK2 = pygame.USEREVENT + 2

#---Block Speed Variables---
startingticktime1 = 500
startingticktime2 = 500
currenttime1 = startingticktime1
currenttime2 = startingticktime2
#Fastest the blocks can go
speedlimiter = 150

#This is the percentage by which the speed increases when a line is cleared 
decrease_factor = 0.10

pygame.time.set_timer(TICK1, currenttime1)
pygame.time.set_timer(TICK2, currenttime2)


#--Block Variables--
block_manager1 = block_manager(g1)
block_manager2 = block_manager(g2)

block_manager1.spawn_block()
block_manager2.spawn_block()


line_due1 = False
line_due2 = False

line_sound = pygame.mixer.Sound("Assets/line.wav")

pygame.font.init()
game_over_text = pygame.font.SysFont('Helvetica', 32)

game_over_condition = False

while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        #Called when the currently falling block lands - saves performance by not having a for loop every frame
        if events.type == TICK1:
            if(block_manager1.get_current_block().move(0,-1) == False):
                pygame.time.set_timer(TICK1, currenttime1)
                if(line_due1 == True):
                    g1.move_up()
                    line_due1 = False
                
                block_manager1.spawn_block()
                
                if(g1.clear_all_lines()):
                    #Called when there are lines to clear
                    if(currenttime1 > speedlimiter):
                        currenttime1 -= int(startingticktime1*decrease_factor)
                    pygame.time.set_timer(TICK1, currenttime1)
                    line_due2 = True
                    line_sound.play()
                
                #Check if block is at the top line; if it is, lose the game and end the game
                for x in range(g1.get_width()):
                    if(g1.graphics_grid[x][g1.get_height()-1].block_present == True):
                        currenttime1 = 0
                        currenttime2 = 0
                        pygame.time.set_timer(TICK1, currenttime1)
                        pygame.time.set_timer(TICK2, currenttime2)
                        pygame.time.wait(100)
                        gameover_image = pygame.image.load("Assets/Player2Won.png")
                        gameover_image = pygame.transform.scale(gameover_image, (900, 700))
                        game_over_condition = True
                
               
        if events.type == TICK2:
            #Called when the currently falling block lands - saves performance by not having a for loop every frame
            if(block_manager2.get_current_block().move(0,-1) == False):
                pygame.time.set_timer(TICK2, currenttime2)

                if(line_due2 == True):
                    g2.move_up()
                    line_due2 = False
                
                block_manager2.spawn_block()
                
                if(g2.clear_all_lines()):
                    #Called when there are lines to clear
                    if(currenttime1 > speedlimiter):
                        currenttime2 -= int(startingticktime2*decrease_factor)
                    pygame.time.set_timer(TICK2, currenttime2)
                    line_due1 = True                
                    line_sound.play()

                #Check if block is at the top line; if it is, lose the game and end the game
                for x in range(g2.get_width()):
                    if(g2.graphics_grid[x][g2.get_height()-1].block_present == True):
                        currenttime1 = 0
                        currenttime2 = 0
                        pygame.time.set_timer(TICK1, currenttime1)
                        pygame.time.set_timer(TICK2, currenttime2)
                        pygame.time.wait(100)
                        scene.fill([100,100,100])

                        #Game Over
                        gameover_image = pygame.image.load("Assets/Player1Won.png")
                        gameover_image = pygame.transform.scale(gameover_image, (900, 700))
                        game_over_condition = True


        FirstPlayerInput(block_manager1.get_current_block())
        SecondPlayerInput(block_manager2.get_current_block())
        if(game_over_condition):
            scene.blit(gameover_image, (0,0))
        
        

    pygame.display.update()
    
