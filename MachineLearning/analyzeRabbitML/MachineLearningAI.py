# 100 - 87
# 20 - 86
# 500 - 87

from sklearn.neural_network import MLPClassifier
import random

data = []
dataTest = []

with open("datasets/dataRabbits.txt", "r") as file:
    for l in file.readlines():
        data.append( (list(map(lambda x:float(x),l.split())), 1))
print("Rabbit data complete")
with open("datasets/dataNoRabbits.txt", "r") as file:
    for l in file.readlines():
        data.append( (list(map(lambda x:float(x),l.split())),0))
print("No rabbit data complete")
with open("datasets/dataTestNoRabbit.txt", "r") as file:
    for l in file.readlines():
        dataTest.append( (list(map(lambda x:float(x),l.split())),0))
print("Test rabbit complete")
with open("datasets/dataTestRabbits.txt", "r") as file:
    for l in file.readlines():
        dataTest.append( (list(map(lambda x:float(x),l.split())),1))
print("Test no rabbit complete")
random.shuffle(data)
random.shuffle(dataTest)
X=[]
y = []

testX = []
testY = []

for d in data:
    X.append(d[0])
    y.append(d[1])

for test in dataTest:
    testX.append(test[0])
    testY.append(test[1])

model = MLPClassifier(random_state=1, max_iter=100)
print("Start Learning")
model.fit(X,y)

predictions = model.predict(testX)
sp = []
for i in range(10000):
    if i%250 == 0:
        sp.append(1.0)
    else:
        sp.append(0.0)
print(model.predict([sp]))
wrong = 0
for p in range(len(predictions)):
    if testY[p] !=predictions[p]:
        wrong+=1
print("SCORE:", round(1 - wrong/len(predictions), 3))

print(model.score(testX,testY))


