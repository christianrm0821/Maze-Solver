from Window import Window
from Line import *
from Point import *

def main():
    win= Window(800,600)

    my_line = Line(Point(0,0),Point(800,600))
    my_line2 = Line(Point(0,0),Point(700,300))
    win.draw_line(my_line,"red")
    win.draw_line(my_line2,"red")



    win.wait_for_close()



main()