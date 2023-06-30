from tkinter import *
import numpy as np


class Creations:
    def creatingCircle(self,x, y, color, radius):
        newRadius = np.ceil(radius/2)
        self.canvas.create_oval(x - newRadius, y - newRadius, x + newRadius, y + newRadius, outline=color, fill=color, width=1)
        self.file.write(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{color}" stroke="{color}"/>\n')
        self.root.update()
    def creatingRabit(self, coordsSet):
        for i in range(len(coordsSet)):
            self.canvas.create_line(coordsSet[i][0], coordsSet[i][1], coordsSet[i - 1][0], coordsSet[i - 1][1], width=2,
                               fill="yellow")
            self.file.write(f'<line x1="{coordsSet[i][0]}" x2="{coordsSet[i - 1][0]}" y1="{coordsSet[i][1]}" y2="{coordsSet[i - 1][1]}" stroke-width="2" stroke="yellow"/>\n')
            self.canvas.create_oval(coordsSet[i][0] - 2, coordsSet[i][1] - 2, coordsSet[i][0] + 2, coordsSet[i][1] + 2,
                               width=2, fill="yellow", outline="yellow")
            self.file.write(f'<circle cx="{coordsSet[i][0]}" cy="{coordsSet[i][1]}" r="2" fill="yellow" stroke="yellow"/>\n')



    def createPoints(self,coordsSet, testSet):
        self.creatingRabit(coordsSet)
        #self.creatingRabit(testSet)
        self.file.write("</svg>\n")
        self.file.close()
        self.root.mainloop()

    def __init__(self, size):
        self.file = open("geometryNN/data/rabbit.svg", "w")
        self.file.write('<?xml version="1.0" standalone="no"?>\n')
        self.file.write('<svg width="500" height="500" version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
        self.root = Tk()
        self.canvas = Canvas(self.root, width=size, height=size, bg="lightgrey")
        self.canvas.pack()




