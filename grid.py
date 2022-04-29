import pygame


class Grid:
    '''Creates a grid height blocks tall and width blocks wide, each block being pixelheight in height and pixelwidth in width.'''
    def __init__(self, screen : pygame.display.set_mode, height: int, width : int, pixelheight : int, pixelwidth : int, left : int, top : int, color : list):
        
        self.screen = screen
        self.height = height
        self.width = width
        self.pixelheight = pixelheight
        self.pixelwidth = pixelwidth
        self.left = left
        self.top = top
        self.color = color
        self.grid = dict()
        #Error Checking
        if(left > screen.get_height() or left < 0 or top < 0 or top > screen.get_height()):
            raise ValueError("Grid: Left {} and Top {} values are out of range!".format(left, top))
    def setup(self):
        '''Draws the grid outline.'''
        for x in range(self.width):
            self.grid[x] = [0] * self.height
        
        for y_pos in range(self.height):
            for x_pos in range(self.width):
                rectangle = pygame.Rect(self.left+x_pos*self.pixelwidth, self.top-y_pos*self.pixelheight, self.pixelwidth, self.pixelheight)
                pygame.draw.rect(self.screen,self.color, rectangle, 2)
                self.grid[x_pos][y_pos] = rectangle
    
    def update(self, position, new_color,w):
        '''Takes a position in the form (x,y) and redraws that grid position with a new color.'''
        pygame.draw.rect(self.screen, new_color, self.grid[position[0]][position[1]],w)
    def clear(self, position):
        '''Takes a position in the form (x,y) and clears that grid position.'''
        #Draws a black square and then places the white outline back over it 
        pygame.draw.rect(self.screen, [0,0,0],self.grid[position[0]][position[1]])
        pygame.draw.rect(self.screen,self.color,self.grid[position[0]][position[1]],2)
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width

        
