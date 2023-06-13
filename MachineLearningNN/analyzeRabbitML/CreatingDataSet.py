import random
import numpy as np

def creatingRabbit(startX,startY, amount):
    if startX + 1 >= amount or startY + 1 >= amount:
        return None
    lenght = random.randint(1,amount-1)
    while startX + lenght >= amount or startY + lenght >= amount:
        lenght = random.randint(1, amount - 1)
    def setRabbit(x, y):

        return startX <= x <= startX + lenght and startY <= y <= startY + lenght


    return setRabbit


def creatingRandomFigure(startX,startY, maximum):

    c = random.choice([1,2,3])
    if c == 1:
        coords = []
        for i in range(random.randint(2,maximum)):
            for y in range(int(startY - np.floor((i*2+1)/2)), int(startY+np.ceil(i*2+1)/2)+1):
                coords.append((startX+i,y))

        def setNoRabbit(x, y):
            if (x, y) in coords:
                return True
            else:
                return False

    elif c==2:
        r = random.randint(2,maximum-1)
        def setNoRabbit(a, b):
            distance = np.sqrt((a - startX) ** 2 + (b - startY) ** 2)

            return distance <= r

    else:
        height,width = 0,0
        while height == width or startX + width > maximum:
            width = random.randint(1, maximum-startX)
        while height==width or startY + height > maximum:
            height = random.randint(1, maximum-startY)
        def setNoRabbit(x, y):
            if x >= startX and x <= startX + width and y >= startY and y <= startY + height:
                return True
            else:
                return False

    return setNoRabbit









def generatingFigure(figure, amount):
    string = ""

    for x in range(amount):
        for y in range(amount):
            if figure(x, y):

                string += "1 "
            else:

                string += "0 "

    return string

class GeneratingRabbits:

    def __init__(self, amount):
        self.amount = int(np.sqrt(amount))
        self.count = amount
        self.test = amount//self.amount
        self.generatingRabbits()
        self.generatingNoRabbits()

    def generatingRabbits(self):
        rabbits = []
        for x in range(self.amount):
            for y in range(self.amount):
                figure = creatingRabbit(x,y, self.amount)
                if figure == None:
                    string =  "0 "* (self.amount*self.amount)
                else:
                    string = generatingFigure(figure, self.amount)



                rabbits.append(string)
            print(len(rabbits))

        random.shuffle(rabbits)
        self.count = len(rabbits)
        rabbits = list(map(lambda x: x + " \n", rabbits))
        testRabbits = []
        for i in range(self.test):
            testRabbits.append(rabbits.pop(0))

        file = open("datasets/dataRabbits.txt", "w")
        file.writelines(rabbits)


        rabbits.clear()
        file.close()

        fileTest = open("datasets/dataTestRabbits.txt", "w")
        fileTest.writelines(testRabbits)
        fileTest.close()



    def generatingNoRabbits(self):
        noRabbits = []
        for x in range(self.amount):
            for y in range(self.amount):
                figure = creatingRandomFigure(x,y,self.amount)

                string = generatingFigure(figure, self.amount)


                noRabbits.append(string)
            print(len(noRabbits))

        random.shuffle(noRabbits)
        noRabbits = random.sample(noRabbits, self.count)
        noRabbits = list(map(lambda x: x + " \n", noRabbits))
        testNoRabbits = []
        for i in range(self.test):
            testNoRabbits.append(noRabbits.pop(0))


        file = open("datasets/dataNoRabbits.txt", "w")
        file.writelines(noRabbits)

        noRabbits.clear()
        file.close()

        fileTest = open("datasets/dataTestNoRabbit.txt", "w")
        fileTest.writelines(testNoRabbits)
        fileTest.close()




