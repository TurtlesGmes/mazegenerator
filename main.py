import pygame
import random

pygame.init()


class cell():
    def __init__(self, sou):
        self.sou = sou
        self.walls = {"right": True, "left": True, "top": True, "bottom": True}
        self.color = (255, 255, 255)
        self.visited = False

    def blit(self, screen, scale):
        x, y = self.sou[0]*scale, self.sou[1]*scale
        if self.walls["right"]:
            pygame.draw.line(screen, self.color, (x+scale, y), (x+scale, y+scale), 5)
        if self.walls["left"]:
            pygame.draw.line(screen, self.color, (x, y), (x, y+scale), 5)
        if self.walls["bottom"]:
            pygame.draw.line(screen, self.color, (x, y+scale), (x+scale, y+scale), 5)
        if self.walls["top"]:
            pygame.draw.line(screen, self.color, (x, y), (x+scale, y), 5)

    def choose_direction(self, cols, rows):
        top = self.check_cell(self.sou[0], self.sou[1]-1, cols, rows)
        bottom = self.check_cell(self.sou[0], self.sou[1]+1, cols, rows)
        left = self.check_cell(self.sou[0]-1, self.sou[1], cols, rows)
        right = self.check_cell(self.sou[0] + 1, self.sou[1], cols, rows)

        neighbors = []
        if top != False and top.visited == False:
            neighbors.append(top)
        if bottom != False and bottom.visited == False:
            neighbors.append(bottom)
        if left != False and left.visited == False:
            neighbors.append(left)
        if right != False and right.visited == False:
            neighbors.append(right)

        if neighbors:
            return random.choice(neighbors)
        else:
            return False
        


    def check_cell(self, x, y, cols, rows):
        if x < 0 or x >= cols or y < 0 or y >= rows:
            return False
        
        print(x + y*cols)
        return cells[x + y*cols]

def start(cols, rows, scale):
    global cells, stack, current_cell
    cells = []
    for row in range(rows):
        for col in range(cols):
            cells.append(cell((col, row)))

    current_cell = cells[0]
    stack = []

def walls_delete(cel, next_cel):
    dx = cel.sou[0] - next_cel.sou[0]
    dy = cel.sou[1] - next_cel.sou[1]
    if dx == 1:
        cel.walls["left"] = False
        next_cel.walls["right"] = False
    if dx == -1:
        cel.walls["right"] = False
        next_cel.walls["left"] = False
    if dy == 1:
        cel.walls["top"] = False
        next_cel.walls["bottom"] = False
    if dy == -1:
        cel.walls["bottom"] = False
        next_cel.walls["top"] = False
        



#velikost okna
height, width = 640, 360

screen = pygame.display.set_mode((width, height))

beckround_color = (0, 0, 0)

tile = 30
cols, rows = width//tile, height//tile
print(cols, rows)

start(cols, rows, tile)

while True:
    screen.fill(beckround_color)

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for cel in cells:
        cel.blit(screen, tile)

    current_cell.visited = True
    next_call = current_cell.choose_direction(cols, rows)

    if next_call:
        walls_delete(current_cell, next_call)
        stack.append(current_cell)
        current_cell = next_call
    elif len(stack) > 0:
        current_cell = stack.pop()

    pygame.display.flip()