import numpy as np
import random

class Board:
    def __init__(self, size, positions):
        self.size = size
        self.positions = positions
        self.board = np.zeros(shape=size)
    
    def move(self, position):
        if not (position[0] >= self.size[0] or position[1] >= self.size[1]):
            switch_coords = [position]
            if position[0] > 0:
                switch_coords.append((position[0]-1, position[1]))
            if position[0] < self.size[0]-1:
                switch_coords.append((position[0]+1, position[1]))
            if position[1] > 0:
                switch_coords.append((position[0], position[1]-1))
            if position[1] < self.size[1]-1:
                switch_coords.append((position[0], position[1]+1))
            
            for coord in switch_coords:
                self.board[coord[1]][coord[0]] += 1
                if self.board[coord[1]][coord[0]] >= self.positions:
                    self.board[coord[1]][coord[0]] = 0
    
    def scramble(self):
        average = self.size[0]*self.size[1]*self.positions
        turns = random.randint(int(0.75*average), int(1.25*average))
        for _ in range(turns):
            self.move((random.randint(0,self.size[0]),random.randint(0,self.size[1])))
    
    def check_solved(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.board[i][j] != self.board[0][0]:
                    return False
        
        return True