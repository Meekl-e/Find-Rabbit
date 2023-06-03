import elementLib
import analyzePoints

# класс проверки фигуры


class checkPoints:

    def __init__(self, coordsSet):
        ap = analyzePoints.AnalyzePoints()
        self.elements = []
        self.mainElements = []
        self.antiElements = []
        self.neirons = []
        # Первый слой, строим общую невыпуклость
        self.antiNeirons = ap.analyzePoint(coordsSet)
        # Второй слой нейронов, которые при выделнии говорят, где в невыпуклых антинейронах есть заяц
        for figure in self.antiNeirons:

            figures = ap.analyzePoint(figure)
            for e in figures:
                self.neirons.append(e)
        # Создание матрицы

        for i in range(1,361):
            e = elementLib.DecisiveFunction(id=i,coordsSet=coordsSet)
            self.mainElements.append(e)

        for n in self.neirons:
            elementFigure = []
            for i in range(1, 361):
                e1 = elementLib.DecisiveFunction(id=i,coordsSet=n)
                elementFigure.append(e1)
            self.elements.append(elementFigure)

        for n in self.antiNeirons:
            elementFigure = []
            for i in range(1, 361):
                e = elementLib.DecisiveFunction(id=i,coordsSet=n)
                elementFigure.append(e)
            self.antiElements.append(elementFigure)







    # Разделено для логического удобства

    def getAntiFiguresPos(self,x,y):

        for figure in self.antiElements:

            summ = 0
            for e in figure:
                res = e.getPos(x, y)
                summ += res
            if summ == 0:
                return False


        return True
    def getFigurePos(self,x,y):

        for figure in self.elements:
            summ = 0
            for e in figure:
                res = e.getPos(x,y)
                summ+=res
            if summ == 0:
                return True
        return False

    # Проверка точки
    def getAllPos(self,x,y):
        for e in self.mainElements:
            res = e.getPos(x,y)
            if res >0:
                return False
        antiRes =  self.getAntiFiguresPos(x,y)
        res =  self.getFigurePos(x,y)
       # print(antiRes,"antiRes")
        #print(res,"res")
        if antiRes == False and res == False:
            return False
        elif antiRes == False and res == True:
            return True
        return True