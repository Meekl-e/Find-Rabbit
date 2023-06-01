import numpy
import elementLib


def getDistance(coords1,coords2):
    return round(numpy.sqrt((coords2[0] -coords1[0]) ** 2 + (coords2[1] - coords1[1]) ** 2), 3)


class AnalyzePoints:
    '''
    def setOrder(self,coordsSet):
        point = coordsSet.pop(coordsSet.index(min(coordsSet)))
        orderedCoords = []
        orderedCoords.append(point)

        for i in range(len(coordsSet)):
            pathsPoints = list(
                map(lambda x: (x, getDistance(x,point)), coordsSet))
            minPoint = min(map(lambda x: x[1], pathsPoints))

            for p in pathsPoints:
                if p[1] == minPoint:
                    point = p[0]
                    coordsSet.remove(point)
                    orderedCoords.append(point)
                    break
        return tuple(orderedCoords)
    '''

    def getAnalyzePoint(self, centerPoint, index, orderedCoords):

        point = orderedCoords[index]
        leftPoint = orderedCoords[index - 1]
        if index != len(orderedCoords) - 1:

            rightPoint = orderedCoords[index + 1]
        else:
            rightPoint = orderedCoords[0]

        centralPoint = ((leftPoint[0] + rightPoint[0]) / 2, (leftPoint[1] + rightPoint[1]) / 2)

        if getDistance(centralPoint, centerPoint) > getDistance(point, centerPoint):
            return True
        return False

    # анализируем точки, на "невыпкулость"
    def analyzePoint(self, orderedCoords):

        centerPoint = (sum(map(lambda x:x[0], orderedCoords))/len(orderedCoords), sum(map(lambda x:x[1], orderedCoords))/len(orderedCoords))

        specifPoints = []
        figures = []
        for index in range(len(orderedCoords)):
            if self.getAnalyzePoint(centerPoint, index, orderedCoords):
                specifPoints.append(orderedCoords[index])



        for p in range(len(orderedCoords)):
            if orderedCoords[p] in sum(figures, []):
                continue

            figure = []
            add = p-1
            while orderedCoords[add] in specifPoints:
                figure.append(orderedCoords[add])
                add-=1
            figure.append(orderedCoords[add])
            figure.reverse()
            add = p
            while orderedCoords[add] in specifPoints:
                figure.append(orderedCoords[add])
                add+=1
                if add == len(orderedCoords):
                    add = 0
            figure.append(orderedCoords[add])
            if len(figure)!=0:
                figures.append(figure)
        print(sum(figures, []))





        # возвращаем список невыпуклых точек
        return tuple(figures)







    def __init__(self, coordsSet):

        figures =  self.analyzePoint(coordsSet)
        self.elements = []
        self.mainElements = []
        for j in range(1, 361):  # 360,180,175,90, 100]:
            element = elementLib.DecisiveFunction(j, coordsSet)
            self.mainElements.append(element)
        for figure in figures:
            elementFigure = []
            for j in range(1, 361):  # 360,180,175,90, 100]:
                element = elementLib.DecisiveFunction(j, figure)
                elementFigure.append(element)

            self.elements.append(elementFigure)



    def getFiguresPos(self,x,y):

        for figure in self.elements:
            summ = 0
            for e in figure:
                res = e.getPos(x, y)
                summ += res
            if summ == 0:
                return True


        return False

    def getAllPos(self,x,y):
        for e in self.mainElements:
            res = e.getPos(x,y)
            if res ==1:
                return False
        if self.getFiguresPos(x,y):
            return False
        return True

        #print(orderedCoords,[specPoints])





