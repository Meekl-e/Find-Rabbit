from tkinter import *



xSet = []
ySet = []

def saving():
    with open("data/data.txt", "w") as file:
        for x,y in zip(xSet, ySet):
            file.write(str(x) + " "+  str(y) + "\n")


def remove():
    f =  open("data/data.txt", "w")
    f.close()

def load():
    canvas.delete("all")
    with open("data/data.txt", "r") as file:
        for str in file.readlines():
            str = str.split()
            creating_figure(int(str[0]),int(str[1]) )


def creating_figure(x,y):
    canvas.delete("all")
    xSet.append(x)
    ySet.append(y)
    for i in range(len(xSet)):
        canvas.create_oval(xSet[i]-1, ySet[i]-1, xSet[i]+1, ySet[i]+1, outline="black",
                           width=5)
        canvas.create_line(xSet[i], ySet[i], xSet[i - 1], ySet[i - 1], width=2, fill="black")


def event(event):
    #canvas.create_oval(event.x-1,event.y-1,event.x+1,event.y+1, width=2)
    file = open("data/data.txt", "a")
    file.write(str(event.x)+" " + str(event.y)+"\n")
    file.close()
    creating_figure(event.x, event.y)


root = Tk()
root.resizable(width=FALSE, height=FALSE)

btns = Frame(root, height=50)
save = Button(btns, text="Save to file", width=10,  font=("Georgia", 16, "bold"), command=saving)
delete = Button(btns,  text="Delete file", width=10, font=("Georgia", 16, "bold"), command=remove)
load = Button(btns, text="Load from file", width=13, font=("Georgia", 16, "bold"), command=load)

btns.pack(fill=X)
save.pack(side=LEFT)
load.pack(side=LEFT)
delete.pack(side=LEFT)

canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack()

canvas.bind("<Button-1>", event)

root.mainloop()


