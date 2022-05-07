import pygame
import grid

class block:

    def __init__(self, grid, letter, color):
        self.color = color
        self.grid = grid
        if(letter == "I"):
            self.blockdef = {2: [0,1,2,3]}
        if(letter == "L"):
            self.blockdef = {0 : [1,2], 1 : [1], 2 : [1]}
    def draw(self):
        for x in self.blockdef:
            for y in self.blockdef[x]:
                self.grid.fill((x,y), self.color)