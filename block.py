import pygame
import grid

class block:

    def __init__(self, grid, letter, color):
        self.grid = grid
        if(letter == "I"):
            self.blockdef = {2: [0,1,2,3]}
            self.color = [100,200,100]
        if(letter == "S"):
            self.blockdef = {0:[1], 1:[1,2], 2:[2]}
        if (letter == "T"):
            self.blockdef = {0:[2], 1:[1,2], 2:[2]}
        if(letter== "O"):
            self.blockdef={3:[0,1],4:[0,1]}
        if(letter== "J"):
            self.blockdef={0:[2],1:[2],3:[1,2]}
            self.color = [0,0,255]
        if(letter == "Z"):
            self.blockdef ={0:[2],1:[1,2],2:[1]}
            self.color = [255,0,0]
        if(letter == "L"):
            self.blockdef = {0 : [1,2], 1: [2], 2: [2] ,3 : [2]}
            self.color = [255, 128, 0]
    def draw(self):
        for x in self.blockdef:
            for y in self.blockdef[x]:
                self.grid.fill((x,y), self.color)