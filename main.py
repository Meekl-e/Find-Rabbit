# Основная часть программы
import elementLib # импортируем класс нейрона
from tkinter import * # импортируем библиотеку для работы с окнами
import creations
import time

# список кортежей координат точек.
coordsSet = []

# создаем визуал
root = Tk()
canvas = Canvas(root, width=500, height=500, bg="lightgrey")
canvas.pack()



# добавляем в общий список точек точки
with open("data/data.txt","r") as file:
    for str in file.readlines():
        str = str.split()
        x = int(str[0])
        y = int(str[1])

        canvas.create_oval(x-1, y-1, x+1,y+1, outline="yellow", width=5)
        coordsSet.append((x,y))


# создаем матрицу нейронов (пока пустая)
elements = []

# заполняем матрицу нейронами
creations.setAll()
#for i in range(len(coordsSet)):

#  Цикл от 1 угла до 360 (включительно)
for j in range(1,361):#360,180,175,90, 100]:
    element = elementLib.DecisiveFunction(j, coordsSet)
    elements.append(element)


#Проверяем для конкретной точки
'''
x = 200
y = 200
rabbit = True

for e in elements:

    # "Спрашиваем" нейрон, является ли по его мнению точка зайцем или нет
    res = e.getPos(x,y)
    # Если не является, то значит точка не заяц
    if res == 0:
        rabbit = False
    # Рисуем черную точку - не заяц
if rabbit == False:
    canvas.create_oval(x-2,y-2,x+2,y+2,outline="white",fill="white", width=2)

    #Если все нейроны согласились, то рисуем желтую точку - точка зайца
else:
    canvas.create_oval(x-2,y-2,x+2,y+2,outline="black",fill="black",width=2)
root.update()

'''

# анализируем холст на фигуры
# Черный - заяц
# Белый - не заяц
for y in range(0,500,4):
    for x in range(0,500,4):
        # обращаемся к каждому нейрону в матрице
        for e in elements:
            # "Спрашиваем" нейрон, является ли по его мнению точка зайцем или нет
            res = e.getPos(x,y)
            # Если не является, то значит точка не заяц
            if res == 0:
                # Рисуем черную точку - не заяц
                canvas.create_oval(x-2,y-2,x+2,y+2,outline="white",fill="white", width=2)
                break
        #Если все нейроны согласились, то рисуем желтую точку - точка зайца
        else:
            canvas.create_oval(x-2,y-2,x+2,y+2,outline="black",fill="black",width=2)
        root.update()

# исуем зайца
for i in range(len(coordsSet)):
    canvas.create_line(coordsSet[i][0], coordsSet[i][1], coordsSet[i-1][0],coordsSet[i-1][1], width=2, fill="yellow")
    canvas.create_oval(coordsSet[i][0]-2, coordsSet[i][1]-2, coordsSet[i][0]+2,coordsSet[i][1]+2, width=2, fill="yellow", outline="yellow")


#бесконечный цикл для окна
root.mainloop()
