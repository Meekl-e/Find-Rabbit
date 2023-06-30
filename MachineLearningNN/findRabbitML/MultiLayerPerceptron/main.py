import CreatingDataSet
from neuralNetwork import NeuralNetwork
import creations

SIZE = 50

def rabbitFunc(x,y):
    return 10 < x < 30 and 10 < y < 30

# создаем файлы
print("Creating data set...")
gen = CreatingDataSet.GeneratingPoints(rabbitFunc,SIZE)

print("Loading data set...")
# берем информацию
dataX, dataY, dataTestX, dataTestY = CreatingDataSet.getData()






# Создаем нейросеть
model = NeuralNetwork(2,1000,[4,2])
print("Start Learning")
model.fit(dataX,dataY)

predictions = model.test(dataTestX)
wrong = 0
for p in range(len(predictions)):
    if dataTestY[p] != predictions[p]:
       wrong += 1

print("SCORE:", round(1 - wrong / len(predictions), 3))


root = creations.Creations(SIZE)

for y in range(0,SIZE,1):
    for x in range(0,SIZE,1):
        if model.test([(x,y)])==[1]:
            root.creatingCircle(x,y, "black")
        else:
            root.creatingCircle(x, y, "white")

root.root.mainloop()
