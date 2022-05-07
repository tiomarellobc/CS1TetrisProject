import pygame
import grid

class block:

    def __init__(self, grid, letter):
        self.grid = grid
        if(letter == "I"):
            self.blockdef = {2: [0,1,2,3]}
        if(letter== "O"):
            self.blockdef={3:[0,1],4:[0,1]}
    def draw(self):
        for x in self.blockdef:
            for y in self.blockdef[x]:
                self.grid.fill((x,y), [100,100,100])