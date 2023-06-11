# Основная часть программы

from RabbitAnalyze import analyzeRabbit
from RabbitAnalyze.classes import figuresCheck
from Utilites import creations as visual

# список кортежей координат точек.
coordsSet = []
coordsTest = []

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

with open("data/dataTest.txt","r") as file:
    for str in file.readlines():
        str = str.split()
        x = int(str[0])
        y = int(str[1])
        coordsTest.append((x,y))






coordsSet = list(coordsSet)
coordsTest = list(coordsTest)

analyzeFigure = figuresCheck.checkPoints(coordsSet)
setRabbit = analyzeRabbit.analyzeRabbit(coordsSet, analyzeFigure)

# анализируем холст на фигуры
# Черный - заяц
# Белый - не заяц
for y in range(0,500,5):
    for x in range(0,500,5):
        if analyzeFigure.getAllPos(x, y):
            root.creatingCircle(x, y, "black")
        else:
            root.creatingCircle(x, y, "white")

# Проверка для какой-то точки
#x = 120
#y = 140
#if analyzeFigure.getAllPos(x,y):
 #   root.creatingCircle(x,y,"black")
#else:
 #   root.creatingCircle(x,y,"white")

print(setRabbit.testFigure(coordsTest))
root.createPoints(coordsSet, coordsTest)



#Проверяем на "медведя"






