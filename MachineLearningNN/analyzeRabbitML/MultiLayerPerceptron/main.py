from MachineLearningNN.analyzeRabbitML import CreatingDataSet
from MachineLearningNN.analyzeRabbitML.MultiLayerPerceptron.neuralNetwork import NeuralNetwork
import random
import numpy as np


# создаем файлы
gen = CreatingDataSet.GeneratingRabbits(500)
# берем информацию


data, dataTest = [],[]
with open("datasets/dataRabbits.txt", "r") as file:
    for l in file.readlines():
        data.append((list(map(lambda x: float(x), l.split())), 1))
print("Rabbit data complete")
with open("datasets/dataNoRabbits.txt", "r") as file:
    for l in file.readlines():
        data.append((list(map(lambda x: float(x), l.split())), 0))
print("No rabbit data complete")
with open("datasets/dataTestNoRabbit.txt", "r") as file:
    for l in file.readlines():
        dataTest.append((list(map(lambda x: float(x), l.split())), 0))
print("Test rabbit complete")
with open("datasets/dataTestRabbits.txt", "r") as file:
    for l in file.readlines():
        dataTest.append((list(map(lambda x: float(x), l.split())), 1))
print("Test no rabbit complete")

random.shuffle(data)
random.shuffle(dataTest)
dataX = []
dataY = []

testX = []
testY = []

for d in data:
    dataX.append(d[0])
    dataY.append(d[1])

for test in dataTest:
    testX.append(test[0])
    testY.append(test[1])




dataX = np.array(dataX)
dataY = np.array(dataY)
testY = np.array(testY)
testX = np.array(testX)


# Создаем нейросеть
model = NeuralNetwork(2,1000,[4,2])

model.fit(dataX,dataY)

predictions = model.test(testX)
wrong = 0
for p in range(len(predictions)):
    if testY[p] != predictions[p]:
       wrong += 1

print("SCORE:", round(1 - wrong / len(predictions), 3))

