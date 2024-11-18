from tkinter import Tk, BOTH, Canvas
from Line import Line
from Point import *
from Window import *
from Cell import *
from Point import *
import time

class Maze:
    def __init__(self, x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win):
        self.x1 =x1
        self.y1 =y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells =[]

        self.create_cells()

    def create_cells(self):
        if self.num_cols ==0 or self.num_cols == 0:
            return
        
        tmp_x = self.x1
        full_maze = []
        for i in range(self.num_cols):
            each_column = []
            tmp_y = self.y1
            for j in range(self.num_rows):
                new_cell = Cell(self.win)
                new_cell.y1 = tmp_y
                new_cell.x1 = tmp_x
                new_cell.x2 =tmp_x+self.cell_size_x
                new_cell.y2 = tmp_y+self.cell_size_y

                each_column.append(new_cell)
                tmp_y += self.cell_size_y
    
            full_maze.append(each_column)
            tmp_x += self.cell_size_x

        self.cells = full_maze

        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                self.draw_cell(row, col)

    def draw_cell(self,i,j):
        x1 = self.cells[i][j].x1
        y1 = self.cells[i][j].y1
        x2 = self.cells[i][j].x2
        y2 = self.cells[i][j].y2
        self.cells[i][j].draw(x1,y1,x2,y2)
        
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(.02)

            


