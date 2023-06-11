from classes import elementLib


#def getDistance(coords1,coords2):
 #   return round(numpy.sqrt((coords2[0] -coords1[0]) ** 2 + (coords2[1] - coords1[1]) ** 2), 3)

# Все помещено в класс для удобства
class AnalyzePoints:
    '''
    Установление порядка координат. В дальнейшем отказался
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



    def getAnalyzePoint(self, centerPoint, index, orderedCoords,specificPoints):

        point = orderedCoords[index]
        add = index -1
        while orderedCoords[add] in specificPoints:
            add-=1

        leftPoint = orderedCoords[add]
        add = index +1
        if add == len(orderedCoords):
            add = 0
        while orderedCoords[add] in specificPoints:

            add+=1
            if add == len(orderedCoords):
                add=0
        rightPoint = orderedCoords[add]

        centralPoint = ((leftPoint[0] + rightPoint[0]) / 2, (leftPoint[1] + rightPoint[1]) / 2)

        if getDistance(centralPoint, centerPoint) > getDistance(point, centerPoint):
            return True
        return False

'''
    def getPos(self,x,y):
        for e in self.elements:
            if e.getPos(x, y) > 0:
                return False
        return True
    def checkCoord(self,x,y):
        summ = 0
        if self.getPos(x + 1, y) == False:
            summ -= 1
        else:
            summ += 1
        if self.getPos(x - 1, y)== False:
            summ -= 1
        else:
            summ += 1
        if self.getPos(x, y+1) == False:
            summ -= 1
        else:
            summ += 1
        if self.getPos(x, y-1) == False:
            summ -= 1
        else:
            summ += 1
        if summ > 0:
            return True
    # анализируем точки, на "невыпкулость"
    def analyzePoint(self, orderedCoords):
        '''
        Мой способ поиска невыпуклых точек
        centerPoint = ((max(map(lambda x: x[0], orderedCoords)) + min(map(lambda x: x[0], orderedCoords))) // 2, (max(map(lambda x: x[1], orderedCoords)) + min(map(lambda x: x[1], orderedCoords))) // 2)

        specifPoints = []
        figures = []
        correcting = True
        while correcting:
            correcting = False
            for index in range(len(orderedCoords)):
                res = self.getAnalyzePoint(centerPoint, index, orderedCoords,specifPoints)
                if res and orderedCoords[index] not in specifPoints:
                    correcting = True
                    specifPoints.append(orderedCoords[index])
        '''
        specifPoints = []
        figures = []
        self.elements = []
        for i in range(1,361):
            e = elementLib.DecisiveFunction(i, orderedCoords)
            self.elements.append(e)
        for x,y in orderedCoords:
            if self.checkCoord(x,y):
                specifPoints.append((x,y))



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
            if len(figure)>2:
                figures.append(figure)






        # возвращаем список невыпуклых точек
        return figures




















