import pygame

class Grid_Block:

    def __init__(self, rect, color, block_present):
        self.rect = rect
        self.color = color
        self.block_present = block_present

class Grid:
    '''Creates a grid height blocks tall and width blocks wide, each block being pixelheight in height and pixelwidth in width.'''
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
        #Draws a black square and then places the white outline back over it 
        grid_object = self.graphics_grid[position[0]][position[1]]
        grid_object.color = self.background_color
        grid_object.block_present = False

        pygame.draw.rect(self.screen, grid_object.color,grid_object.rect)
        pygame.draw.rect(self.screen,self.grid_color,grid_object.rect,2)

    def get_color(self, position):
        return self.graphics_grid[position[0]][position[1]].color
    
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width

        

