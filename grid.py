from turtle import color
import pygame
import random
class Grid_Block:

    def __init__(self, rect, color, block_present):
        self.rect = rect
        self.color = color
        self.block_present = block_present
    def copy(self, newGrid_Block):
        self.color = newGrid_Block.color
        self.block_present = newGrid_Block.block_present
        

class Grid:
    '''Creates a grid height blocks tall and width blocks wide, each block being pixelheight in height and pixelwidth in width, at the pixel coordinates left and top'''
    def __init__(self, screen : pygame.display.set_mode, height: int, width : int, pixelheight : int, pixelwidth : int, left : int, top : int, color : list, bgcolor : list):
        
        self.screen = screen
        self.height = height
        self.width = width
        self.pixelheight = pixelheight
        self.pixelwidth = pixelwidth
        self.left = left
        self.top = top
        self.grid_color = color
        self.background_color = bgcolor
        self.graphics_grid = dict()

        #Error Checking
        if(left > screen.get_height() or left < 0 or top < 0 or top > screen.get_height()):
            raise ValueError("Grid: Left {} and Top {} values are out of range!".format(left, top))
    def setup(self):
        '''Draws the grid outline.'''
        
        for x in range(self.width):
            self.graphics_grid[x] = [0] * self.height
        
        #Populates the grid dictionary with grid rect objects with default of background_color
        for y_pos in range(self.height):
            for x_pos in range(self.width):
                rectangle = pygame.Rect(self.left+x_pos*self.pixelwidth, self.top-y_pos*self.pixelheight, self.pixelwidth, self.pixelheight)
                pygame.draw.rect(self.screen,self.background_color, rectangle)
                pygame.draw.rect(self.screen,self.grid_color, rectangle, 2)
                self.graphics_grid[x_pos][y_pos] = Grid_Block(rectangle, self.background_color, False)
    
    def fill(self, position, new_color):
        '''Takes a position in the form (x,y) and redraws that grid position with a new color.'''
        grid_object = self.graphics_grid[position[0]][position[1]]
        grid_object.color = new_color
        grid_object.block_present = True
        pygame.draw.rect(self.screen, grid_object.color, grid_object.rect)
    def clear(self, position):
        '''Takes a position in the form (x,y) and clears that grid position.'''
        #Draws a black square and then places the grid color back over it 
        grid_object = self.graphics_grid[position[0]][position[1]]
        grid_object.color = self.background_color
        grid_object.block_present = False

        pygame.draw.rect(self.screen, grid_object.color,grid_object.rect)
        pygame.draw.rect(self.screen,self.grid_color,grid_object.rect,2)

    

    
    def get_color(self, position):
        return self.graphics_grid[position[0]][position[1]].color
    
    def check_valid_position(self, position):
        '''Check if position is inside grid'''
        #Check if x position is inside the grid
        if(position[0] >= 0 and position[0] < self.width):
            #Check if y position is inside the grid
            if(position[1] >= 0 and position[1] < self.height):
                return True
        
        return False
    
    def check_line(self, line):
        '''Returns true if an entire line is occupied, otherwise false.'''
        for i in range(self.width):
            if(self.graphics_grid[i][line].block_present == False):
                return False
        return True
    def clear_line(self, line):
        '''Clears a line and moves the lines above it downward'''

        #Clear the line targeted
        for i in range(self.width):
            self.clear((i,line))
        #Copy the data from the line above, for every line above
        for x in range(self.width):
            for y in range(line, self.height-1):
                self.graphics_grid[x][y].copy(self.graphics_grid[x][y+1])
        #Refill every line with the new data that's been copied to
        for x in range(self.width):
            for y in range(self.height):
                if(self.graphics_grid[x][y].block_present == True):
                    self.fill((x,y), self.graphics_grid[x][y].color)
                else:
                    self.clear((x,y))
    def clear_all_lines(self):
        #Moves downward frmo the top, as this allows 
        cleared_line = False
        for i in range(self.get_height()-1, -1, -1):
                    if(self.check_line(i) == True):
                        self.clear_line(i)
                        cleared_line = True
        print(cleared_line)
        return cleared_line
        
    def move_up(self):
        for x in range(self.width):
            for y in range(self.height-1, 0, -1):
                self.graphics_grid[x][y].copy(self.graphics_grid[x][y-1])
                
        i = random.randint(0, self.width-1)
        for x in range(self.width):
            if(x != i):
                self.graphics_grid[x][0].block_present = True
                self.graphics_grid[x][0].color = [100,100,100]
            if(x == i):
                self.graphics_grid[x][0].block_present = False

        for x in range(self.width):
            for y in range(self.height):
                if(self.graphics_grid[x][y].block_present == True):
                    self.fill((x,y), self.graphics_grid[x][y].color)
                else:
                    self.clear((x,y))
        
        
        
    def check_position_filled(self, position):
        '''Returns whether a block is there'''
        return self.graphics_grid[position[0]][position[1]].block_present
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width

        

