import pygame
import grid

class block:

    def __init__(self, grid, letter):
        self.grid = grid
        if(letter == "I"):
            self.blockdef = {2: [0,1,2,3]}
<<<<<<< HEAD

        if(letter == "J"):
            self.blockdef = {0: [2],1:[2],2:[1,2]}

        if(letter == "Z"):
            self.blockdef = {0:[2],1:[1,2],2:[1]}

        

    
=======
        if(letter== "O"):
            self.blockdef={3:[0,1],4:[0,1]}
>>>>>>> faa7ef6c53738775b7b49a912888468b7f072e7c
    def draw(self):
        for x in self.blockdef:
            for y in self.blockdef[x]:
                self.grid.fill((x,y), [100,100,100])