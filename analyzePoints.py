import numpy

import alphashape

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


        alpha_shape = alphashape.alphashape(orderedCoords, 0)
        # получаем координаты вершин альфа-формы
        vertices = list(alpha_shape.exterior.coords)
        # для каждой точки в фигуре
        for point in orderedCoords:
            # если точка не принадлежит вершинам альфа-формы
            if point not in vertices:
                # добавляем ее в список невыпуклых точек

                specifPoints.append(point)



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




















