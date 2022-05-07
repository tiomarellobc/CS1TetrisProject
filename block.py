import pygame
import grid

class block:

    def __init__(self, grid, letter):
        self.grid = grid
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
        if(letter== "J"):
<<<<<<< HEAD
            self.blockdef= {0:[2],1:[2],3:[1,2]}
=======
            self.blockdef={0:[2],1:[2],3:[1,2]}
        if(letter == "L"):
            self.blockdef = {0 : [1,2], 1: [2], 2: [2] ,3 : [2]}
            self.color = [255, 128, 0]
>>>>>>> caf63a7fa580ba39ce8e2d2a87d6d29b9de84978
    def draw(self):
        for x in self.blockdef:
            for y in self.blockdef[x]:
                self.grid.fill((x,y), color)