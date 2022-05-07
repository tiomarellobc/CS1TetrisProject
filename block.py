import pygame
import grid

class block:

    def __init__(self, grid):
        "..x.",
        "..x.",
        "..x.",
        "..x."
        self.blockdef = {0 : [0], 1 :[0,1], 2: [0]}
        self.g = grid
    
    def draw(self):
        for x in self.blockdef:
            for y in self.blockdef[x]:
                self.g.fill((x,y), [100,100,100])