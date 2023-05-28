import elementLib
import math

class analyzeRabbit():
    def getPos(self, x, y, elements):
        for e in elements:
            # "Спрашиваем" нейрон, является ли по его мнению точка зайцем или нет
            res = e.getPos(x, y)
            # Если не является, то значит точка не заяц
            if res == 0:
                # Рисуем черную точку - не заяц
                return False
            # Если все нейроны согласились, то рисуем желтую точку - точка зайца
        else:
            return True

    def creatingFigure(self, coordsSetStart):
        elements = []
        for j in range(1, 361):  # 360,180,175,90, 100]:
            element = elementLib.DecisiveFunction(j, coordsSetStart)
            elements.append(element)
        coords = []
        for x, y in coordsSetStart:
            summ = 0
            if self.getPos(x + 1, y, elements) == False:
                summ -= 1
            else:
                summ += 1
            if self.getPos(x - 1, y, elements) == False:
                summ -= 1
            else:
                summ += 1
            if self.getPos(x, y - 1, elements) == False:
                summ -= 1
            else:
                summ += 1
            if self.getPos(x, y + 1,elements) == False:
                summ -= 1
            else:
                summ += 1
            if summ <= 0:
                coords.append((x, y))

        centralPointX = (max(map(lambda x: x[0], coords)) + min(map(lambda x: x[0], coords))) // 2
        centralPointY = (max(map(lambda x: x[1], coords)) + min(map(lambda x: x[1], coords))) // 2
        distances = []
        for x, y in coords:
            distances.append(math.sqrt((x - centralPointX) ** 2 + (y - centralPointY) ** 2))

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


    def __init__(self, coordsSetStart):
        self.coordMoving = self.creatingFigure(coordsSetStart)


    def testFigure(self,coordsSetStart):
        figureMoving = self.creatingFigure(coordsSetStart)
        if figureMoving == self.coordMoving:
            return True
        else:
            return False


