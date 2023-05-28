from tkinter import *

def creating_line(p, sin, cos,color, width=1):
    x1 = 0
    x2 = 500

    y1 = p/sin
    y2 =  (p - x2 * cos)/sin

    # для рисования векторов
    #x2 = cos * x+200
    #x1 = 200
   # y1 = 200
    #y2 = y*sin+200



    canvas.create_line(x1,y1,x2,y2, fill=color, width=width)

    root.update()




def setAll():
    global root, canvas
    root = Tk()
    canvas = Canvas(root, width=500, height=500, bg="lightgrey")
    canvas.pack()

