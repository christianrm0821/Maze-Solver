from tkinter import Tk, BOTH, Canvas
from Line import Line
from Point import *
from Window import *

class Cell:
    def __init__(self, window):
        self.has_left_wall =True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1=  None
        self.y2=  None
        self.win = window
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self.win == None:
            return
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        top_line = Line(Point(self.x1,self.y1),Point(self.x2,self.y1))
        bottom_line = Line(Point(self.x1,self.y2), Point(self.x2,self.y2))
        left_line = Line(Point(self.x1,self.y1), Point(self.x1,self.y2))
        right_line = Line(Point(self.x2,self.y1), Point(self.x2,self.y2))
        
        if self.has_top_wall == True:
            self.win.draw_line(top_line,"red")
        else:
            self.win.draw_line(top_line,"white")

        if self.has_bottom_wall == True:
            self.win.draw_line(bottom_line,"red")
        else:
            self.win.draw_line(bottom_line,"white")

        if self.has_left_wall == True:
            self.win.draw_line(left_line,"red")
        else:
            self.win.draw_line(left_line,"white")

        if self.has_right_wall == True:
            self.win.draw_line(right_line,"red")
        else:
            self.win.draw_line(right_line,"white")


    def draw_move(self, to_cell, undo = False):
        curr_center_x = (self.x1 +self.x2)/2
        curr_center_y = (self.y1+self.y2)/2
        to_cell_center_x = (to_cell.x1+to_cell.x2)/2
        to_cell_center_y = (to_cell.y1+to_cell.y2)/2

        if undo == False:
            color = "red"
        else:
            color ="gray"
        
        center_line = Line(Point(curr_center_x,curr_center_y), Point(to_cell_center_x,to_cell_center_y))
        self.win.draw_line(center_line,color)



        


