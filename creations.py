from tkinter import *



class Creations:
    def creatingCircle(self,x, y, color):
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, outline=color, fill=color, width=1)
        self.root.update()
    def creatingRabit(self, coordsSet):
        for i in range(len(coordsSet)):
            self.canvas.create_line(coordsSet[i][0], coordsSet[i][1], coordsSet[i - 1][0], coordsSet[i - 1][1], width=2,
                               fill="yellow")
            self.canvas.create_oval(coordsSet[i][0] - 2, coordsSet[i][1] - 2, coordsSet[i][0] + 2, coordsSet[i][1] + 2,
                               width=2, fill="yellow", outline="yellow")



    def createPoints(self,coordsSet, testSet):
        self.creatingRabit(coordsSet)
        self.creatingRabit(testSet)

        self.root.mainloop()

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=500, height=500, bg="lightgrey")
        self.canvas.pack()



