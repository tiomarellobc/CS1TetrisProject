import pygame
import grid



class block:

    def __init__(self, grid, letter):
        self.currentrot = 0
        self.grid = grid
        self.set_blockdef(letter)
        self.y = 22
        self.x = 4

    def move(self,x : int, y : int):
        '''Moves the block x units and y units. Note: It does not check whether the moved position is a valid position'''

        #Checks if the position that the block will move to is inside the grid
        for xpos in self.blockdef:
            for ypos in self.blockdef[xpos]:
                if(self.grid.check_valid_position((self.x+xpos+x, self.y+ypos+y)) == False):
                    return False
        self.clear()
        #Check if the block has hit another block
        for xpos in self.blockdef:
            for ypos in self.blockdef[xpos]:
                if(self.grid.check_position_filled((self.x+xpos+x, self.y+ypos+y)) == True):
                    self.draw()
                    return False
        
        self.x += x
        self.y += y
        self.draw()

    #TODO: Check if rotation position is a valid position
    def rotate(self, dir : int):
        '''Rotate the block in either direction'''
        prov = self.currentrot
        
        #Check if the provisional rotation is outside the list of rotations, wrap around if it is
        if(self.currentrot + dir >= len(self.blockrots)):
            prov= 0
        elif(self.currentrot + dir < 0):
            prov = len(self.blockrots)-1
        else:
            prov += dir
        temp = self.blockrots[prov]

        #Check if the new rotation is outside the grid by checking each position
        for xpos in temp:
            for ypos in temp[xpos]:
                if(self.grid.check_valid_position((self.x+xpos,self.y+ypos)) == False):
                    return False
        
        self.clear()
        
        #Check if the new rotation is going to intersect with already existing block
        for xpos in temp:
            for ypos in temp[xpos]:
                if(self.grid.check_position_filled((self.x+xpos,self.y+ypos)) == True):
                    self.draw()
                    return False
        self.currentrot = prov
        self.blockdef = self.blockrots[self.currentrot]
        
        self.draw()

    def set_blockdef(self, letter: str):
        '''Takes a string and sets the block to have that tetris piece'''
        #Each block has a list of rotations, which define the block as a series of filled positions in a 8x8 grid.
        #Tio
        if(letter == "I"):
            self.blockrots = [{0 : [2], 1 : [2], 2 : [2], 3 : [2]},{2: [0,1,2,3]}]
            self.color = [0,255,255]
        #Sunderya
        if(letter == "S"):
            self.blockrots = [{0:[1], 1:[1,2], 2:[2]}, {0:[2,3], 1:[1,2]}]
            self.color = [0,255,0]
        #Sunderya
        if (letter == "T"):
            self.blockrots = [{0:[2], 1:[1,2], 2:[2]},{0: [2], 1: [1,2,3]},{0:[1], 1:[1,2], 2:[1]},{1:[1,2,3], 2:[2]}]
            self.color = [127, 0, 255]
        if(letter== "O"):
            self.blockrots= [{1:[0,1],2:[0,1]}]
            self.color = [255,255,0]
        #Linda
        if(letter== "J"):
            self.blockrots=[{0:[2],1:[2],2:[1,2]}, {0:[1],1:[1,2,3]}, {0:[1,2],1:[1],2:[1]},{1:[1,2,3],2:[3]}]
            self.color = [0,0,255]
        #Sunderya
        if(letter == "Z"):
            self.blockrots =[{0:[2],1:[1,2],2:[1]},{1:[1,2], 2:[2,3]}]
            self.color = [255,0,0]
        #Kodee
        if (letter == "L"):
            self.blockrots = [{0 : [1,2], 1: [2], 2: [2]},{0:[3],1:[1,2,3]},{0:[1],1:[1],2:[1,2]},{1:[1,2,3],2:[1]}]
            self.color = [255, 128, 0]
        self.blockdef = self.blockrots[self.currentrot]

    def draw(self):
        '''Uses the blocks current position and color to draw on the screen.'''
        for x in self.blockdef:
            for y in self.blockdef[x]:
                self.grid.fill((self.x+x,self.y+y), self.color)
    def clear(self):
        '''Uses the blocks current position and color to clear itself.'''
        for xpos in self.blockdef:
            for ypos in self.blockdef[xpos]:
                self.grid.clear((self.x+xpos,self.y+ypos))
   