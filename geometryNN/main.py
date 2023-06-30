# Основная часть программы

from RabbitAnalyze import figuresCheck, analyzeRabbit
import creations as visual

#Установить размер холста
size = 500

def loadData():
    coordsTest, coordsSet = [],[]
    with open("geometryNN/data/data.txt", "r") as file:
        for str in file.readlines():
            str = str.split()
            x = int(str[0])
            y = int(str[1])

            coordsSet.append((x, y))
    with open("geometryNN/data/dataTest.txt", "r") as file:
        for str in file.readlines():
            str = str.split()
            x = int(str[0])
            y = int(str[1])
            coordsTest.append((x, y))
    return coordsSet, coordsTest


def checkAllCoords(lenSize):
    for y in range(0, lenSize,3):
        for x in range(0, lenSize, 3):
            if analyzeFigure.getAllPos(x,y):
                root.creatingCircle(x,y,"black")
            else:
                root.creatingCircle(x,y,"white")
def checkCoord(x,y):
    if analyzeFigure.getAllPos(x, y):
        root.creatingCircle(x, y, "black")
    else:
        root.creatingCircle(x, y, "white")


coordsSet, coordsTest = loadData()
root = visual.Creations(size)
analyzeFigure = figuresCheck.checkPoints(coordsSet)
setRabbit = analyzeRabbit.analyzeRabbit(coordsSet, analyzeFigure)
# анализируем холст на фигуры
# Черный - заяц
# Белый - не заяц
checkAllCoords(size)
 # Проверка для какой-то точки
 #checkCoord(1,1)

# Проверяем на "медведя"
print(setRabbit.testFigure(coordsTest))
root.createPoints(coordsSet, coordsTest)




