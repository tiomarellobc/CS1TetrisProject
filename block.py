import pygame
import grid

class block:

    def __init__(self, grid, letter):
        self.grid = grid
        self.set_blockdef(letter)
        self.y = 20
        self.x = 7

    #move in x units, y units
    def move(self,x,y):
        for xpos in self.blockdef:
            for ypos in self.blockdef[xpos]:
                self.grid.clear((self.x+xpos,self.y+ypos))
        self.x += x
        self.y += y
        self.draw()

    def set_blockdef(self, letter):
        if(letter == "I"):
            self.blockdef = {2: [0,1,2,3]}
            self.color = [100,200,100]
        if(letter == "S"):
            self.blockdef = {0:[1], 1:[1,2], 2:[2]}
            self.color = [0,255,0]
        if (letter == "T"):
            self.blockdef = {0:[2], 1:[1,2], 2:[2]}
            self.color = [127, 0, 255]
        if(letter== "O"):
            self.blockdef= {3:[0,1],4:[0,1]}
            self.color = [255,255,0]
        if(letter== "J"):
            self.blockdef={0:[2],1:[2],3:[1,2]}
            self.color = [0,0,255]
        if(letter == "Z"):
            self.blockdef ={0:[2],1:[1,2],2:[1]}
            self.color = [255,0,0]
        if(letter == "L"):
            self.blockdef = {0 : [1,2], 1: [2], 2: [2]}
            self.color = [255, 128, 0]


    def draw(self):
        for x in self.blockdef:
            for y in self.blockdef[x]:
                self.grid.fill((self.x+x,self.y+y), self.color)