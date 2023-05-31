# Основная часть программы
import math

import elementLib # импортируем класс нейрона

import analyzeRabbit
import analyzePoints as rc
import creations as visual



# список кортежей координат точек.
coordsSet = []

# создаем визуал
root = visual.Creations()



# добавляем в общий список точек точки
with open("data/data.txt","r") as file:
    for str in file.readlines():
        str = str.split()
        x = int(str[0])
        y = int(str[1])


        coordsSet.append((x,y))

# добавляем в общий тестовый список точек точки
coordsTest = []
with open("data/dataTest.txt","r") as file:
    for str in file.readlines():
        str = str.split()
        x = int(str[0])
        y = int(str[1])
        coordsTest.append((x,y))







analyzeFigure = rc.AnalyzePoints(coordsSet)
setRabbit = analyzeRabbit.analyzeRabbit(coordsSet, analyzeFigure)

# анализируем холст на фигуры
# Черный - заяц
# Белый - не заяц
for y in range(0,500,5):
    for x in range(0,500,5):
        # обращаемся к каждому нейрону в матрице
        if analyzeFigure.getAllPos(x,y):
            root.creatingCircle(x,y,"black")
        else:
            root.creatingCircle(x,y,"white")

print(setRabbit.testFigure(coordsTest))
root.createPoints(coordsSet, coordsTest)
# исуем зайца


#Проверяем на "медведя"






