from Window import Window
from Line import *
from Point import *
from Cell import *
from Maze import *

def main():
    win= Window(800,600)
    new_maze = Maze(5,5,10,15,50,50,win)
    



    win.wait_for_close()



main()