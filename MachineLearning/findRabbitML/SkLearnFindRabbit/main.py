from sklearn.neural_network import MLPClassifier
from MachineLearning.findRabbitML import CreatingDataSet

gen = CreatingDataSet.GeneratingPoints(2000,500)
X,y,testX,testY = CreatingDataSet.getData()

model = MLPClassifier(random_state=1, max_iter=1000)
print("Start Learning")
model.fit(X, y)

predictions = model.predict(testX)

wrong = 0
for p in range(len(predictions)):
    if testY[p] != predictions[p]:
         wrong += 1

print("SCORE:", round(1 - wrong / len(predictions), 3))

print(model.score(testX, testY))