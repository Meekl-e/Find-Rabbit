from MachineLearning.findRabbitML import CreatingDataSet
from MachineLearning.findRabbitML.MultiLayerPerceptron.neuralNetwork import NeuralNetwork



# создаем файлы
gen = CreatingDataSet.GeneratingPoints(100, 100)

# берем информацию
dataX, dataY, dataTestX, dataTestY = CreatingDataSet.getData()






# Создаем нейросеть
model = NeuralNetwork(2,1000,[4,2])

model.fit(dataX,dataY)

predictions = model.test(dataTestX)
wrong = 0
for p in range(len(predictions)):
    if dataTestY[p] != predictions[p]:
       wrong += 1

print("SCORE:", round(1 - wrong / len(predictions), 3))

