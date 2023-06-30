import random
import numpy as np


def getData():
    data = []
    dataTest = []
    with open("MachineLearningNN/findRabbitML/SkLearnFindRabbit/datasets/dataRabbits.txt", "r") as file:
        for l in file.readlines():
            data.append((list(map(lambda x: float(x), l.split())), 1))

    with open("MachineLearningNN/findRabbitML/SkLearnFindRabbit/datasets/dataNoRabbits.txt", "r") as file:
        for l in file.readlines():
            data.append((list(map(lambda x: float(x), l.split())), 0))

    with open("MachineLearningNN/findRabbitML/SkLearnFindRabbit/datasets/dataTestNoRabbits.txt", "r") as file:
        for l in file.readlines():
            dataTest.append((list(map(lambda x: float(x), l.split())), 0))

    with open("MachineLearningNN/findRabbitML/SkLearnFindRabbit/datasets/dataTestRabbits.txt", "r") as file:
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


def saveToFile(name, data):
    file = open("MachineLearningNN/findRabbitML/SkLearnFindRabbit/datasets/data"+name+".txt", "w")
    for line in data:
        for s in line:
            file.write(str(s)+" ")
        file.write("\n")

    file.close()


class GeneratingPoints:

    def generating(self):
        dataRabbits = []
        dataNoRabbits = []


        for x in range(self.amount):
            for y in range(self.amount):
                if self.rabbitFunc(x, y):
                    dataRabbits.append((x, y))
                else:
                    dataNoRabbits.append((x, y))
        while len(dataNoRabbits) > len(dataRabbits):
            dataNoRabbits.pop(random.randint(0,len(dataNoRabbits)-1))





        self.creatingfile(dataRabbits, "Rabbits")
        self.creatingfile(dataNoRabbits, "NoRabbits")

    def creatingfile(self, data, name):
        random.shuffle(data)


        dataTest = []
        for i in range(len(data)//10):
            dataTest.append(data.pop(0))

        saveToFile(name, data)
        saveToFile("Test"+name, dataTest)





    def __init__(self, rabbitFunc,lenSize = 100,):

        self.rabbitFunc = rabbitFunc
        self.amount = lenSize
        self.generating()











