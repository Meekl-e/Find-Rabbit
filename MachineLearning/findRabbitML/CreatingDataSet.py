import random
import numpy as np


def getData():
    data = []
    dataTest = []
    with open("datasets/dataRabbits.txt", "r") as file:
        for l in file.readlines():
            data.append((list(map(lambda x: float(x), l.split())), 1))

    with open("datasets/dataNoRabbits.txt", "r") as file:
        for l in file.readlines():
            data.append((list(map(lambda x: float(x), l.split())), 0))

    with open("datasets/dataTestNoRabbits.txt", "r") as file:
        for l in file.readlines():
            dataTest.append((list(map(lambda x: float(x), l.split())), 0))

    with open("datasets/dataTestRabbits.txt", "r") as file:
        for l in file.readlines():
            dataTest.append((list(map(lambda x: float(x), l.split())), 1))
    random.shuffle(data)
    random.shuffle(dataTest)
    X = []
    y = []

    testX = []
    testY = []

    for d in data:
        X.append(d[0])
        y.append(d[1])

    for test in dataTest:
        testX.append(test[0])
        testY.append(test[1])

    return np.array(X),np.array(y),np.array(testX),np.array(testY)

def rabbitFunc(x,y):
    r = 100

    distance = np.sqrt((x - 100) ** 2 + (y - 100) ** 2)

    return distance <= r

def saveToFile(name, data):
    file = open("datasets/data"+name+".txt", "w")
    for line in data:
        for s in line:
            file.write(str(s)+" ")
        file.write("\n")

    file.close()


class GeneratingPoints:

    def generating(self):
        dataRabbits = []
        dataNoRabbits = []
        while len(dataRabbits) <= self.amount:
            for i in range(self.amount):
                x = random.randint(0, self.lenSize)
                y = random.randint(0, self.lenSize)
                while (x, y) in dataRabbits or (x, y) in dataNoRabbits:
                    x = random.randint(0, self.lenSize)
                    y = random.randint(0, self.lenSize)
                if rabbitFunc(x, y):
                    dataRabbits.append((x, y))
                else:
                    dataNoRabbits.append((x, y))
            while len(dataNoRabbits) > len(dataRabbits):
                dataNoRabbits.pop(0)
            while len(dataRabbits) > len(dataNoRabbits):
                dataRabbits.pop(0)

        self.creatingfile(dataRabbits, "Rabbits")
        self.creatingfile(dataNoRabbits, "NoRabbits")

    def creatingfile(self, data, name):
        random.shuffle(data)


        dataTest = []
        for i in range(len(data)//10):
            dataTest.append(data.pop(0))

        saveToFile(name, data)
        saveToFile("Test"+name, dataTest)





    def __init__(self, amount=-1, lenSize = 100):

        if amount == -1:
            amount = lenSize**2
        self.amount = amount
        self.lenSize = lenSize
        self.generating()











