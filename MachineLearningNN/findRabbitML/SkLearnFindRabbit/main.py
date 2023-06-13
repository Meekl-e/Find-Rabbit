from sklearn.neural_network import MLPClassifier
from MachineLearningNN.findRabbitML import CreatingDataSet as CreatingFindData
import creations

def rabbitFunc(x,y):
    return 50 < x < 70 and 50 < y < 70

SIZE = 500
print("Creating Points")
gen = CreatingFindData.GeneratingPoints(rabbitFunc,SIZE)
X,y,testX,testY = CreatingFindData.getData()

model = MLPClassifier(random_state=1, max_iter=1000)
print("Start Learning")

model.fit(X, y)

predictions = model.predict(testX)

print("SCORE:",model.score(testX, testY))

root = creations.Creations(SIZE)

for y in range(0,SIZE,3):
    for x in range(0,SIZE,3):
        if model.predict([(x,y)])==1:
            root.creatingCircle(x,y, "black")
        else:
            root.creatingCircle(x, y, "white")

root.root.mainloop()