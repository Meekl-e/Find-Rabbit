from tkinter import *

def creating_line(p,sin, cos):
    x1 = 0
    x2 = 500
    y1 = p/cos
    print((p - x2 * sin)/cos)
    y2 =  (p - x2 * sin)/cos
    canvas.create_line(x1,y1,x2,y2, fill="orange")
    #canvas.create_oval((x+x2/2)-2,(y+y2/2)-2,(x+x2/2)+2,(y+y2/2)+2,  width=2)
    #canvas.create_oval(x  - 2, y - 2, x  + 2, y  + 2)
    root.update()

def setAll():
    global root, canvas
    root = Tk()
    canvas = Canvas(root, width=500, height=500, bg="lightgrey")
    canvas.pack()

