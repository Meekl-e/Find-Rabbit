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

    # анализируем точки, на "невыпкулость"
    def analyzePoint(self, orderedCoords):

        centerPoint = (sum(map(lambda x:x[0], orderedCoords))/len(orderedCoords), sum(map(lambda x:x[1], orderedCoords))/len(orderedCoords))

        specifPoints = []
        for index in range(len(orderedCoords)):
            point = orderedCoords[index]
            leftPoint = orderedCoords[index-1]
            if index != len(orderedCoords)-1:

                rightPoint = orderedCoords[index+1]
            else:
                rightPoint = orderedCoords[0]

            centralPoint = ((leftPoint[0]+rightPoint[0])/2, (leftPoint[1]+rightPoint[1])/2)

            if getDistance(centralPoint, centerPoint) > getDistance(point, centerPoint):

                specifPoints.append((leftPoint,point,rightPoint))
        # возвращаем список невыпуклых точек
        return tuple(specifPoints)







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





