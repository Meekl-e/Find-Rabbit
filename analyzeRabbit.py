
import numpy
import analyzePoints
class analyzeRabbit():


    def creatingFigure(self, coordsSetStart, analyzeFigure):

        coords = []
        for x, y in coordsSetStart:
            summ = 0
            if analyzeFigure.getAllPos(x + 1, y) == False:
                summ -= 1
            else:
                summ += 1
            if analyzeFigure.getAllPos(x - 1, y)== False:
                summ -= 1
            else:
                summ += 1
            if analyzeFigure.getAllPos(x, y+1) == False:
                summ -= 1
            else:
                summ += 1
            if analyzeFigure.getAllPos(x, y-1) == False:
                summ -= 1
            else:
                summ += 1
            if summ <= 0:
                coords.append((x, y))

        centralPointX = (max(map(lambda x: x[0], coords)) + min(map(lambda x: x[0], coords))) // 2
        centralPointY = (max(map(lambda x: x[1], coords)) + min(map(lambda x: x[1], coords))) // 2
        distances = []


        for x, y in coords:
            distances.append(numpy.sqrt((x - centralPointX) ** 2 + (y - centralPointY) ** 2))

        centralVector = 0
        for v in distances:
            centralVector += v
        centralVector /= len(distances)
        coordMoving = []
        for dist in distances:
            if centralVector - dist > 0:
                coordMoving.append(1)
            elif centralVector - dist < 0:
                coordMoving.append(-1)
            else:
                coordMoving.append(0)
        return coordMoving


    def __init__(self, coordsSetStart, analyzeFigure):
        self.coordMoving = self.creatingFigure(coordsSetStart, analyzeFigure)


    def testFigure(self,coordsSetStart):
        figureMoving = self.creatingFigure(coordsSetStart, analyzePoints.AnalyzePoints(coordsSetStart))
        if len(figureMoving)!=len(self.coordMoving):
            return False
        if sum(figureMoving) - sum(self.coordMoving) == 0:
            return True
        return False


