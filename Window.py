from tkinter import Tk, BOTH, Canvas
from Line import Line
from Point import *

class Window:
    def __init__(self,width,height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height, bg ="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running =True
        while self.running:
            self.redraw()
        print("window is closed")


    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas,fill_color)

    def close(self):
        self.running = False
