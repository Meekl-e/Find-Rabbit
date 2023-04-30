# Класс нейрона

import math # испортируем сложные вычисления

# Функция для рассчета максимального значения для всех пробных точек
# Вход: sin угла, cos угла, набор пробных точек
# Максимальное значение из суммы синуса умноженного на xi и косинуса умноженного на yi
def getMaxFromCoords(sin, cos, coordsSet):
    res = []
    for coord in coordsSet:
        res.append(coord[0]*sin + coord[1]*cos)

    return max(res)



# Основной класс нейрона
class DecisiveFunction:

    # Определяющая функция
    # Вход: номер нейрона j, набор пробных точек в формате: [(x1,y1),(x2,y2),...]
    def __init__(self, id, coordsSet):
        self.j = id # Присваиваем j
        self.alpha = 2* 3.14 /  10 * id # Вычисляем угол alpha (каким из углов будет этот нейрон )
        self.sin = math.sin(self.alpha) # Вычисляем sin alpha
        self.cos = math.cos(self.alpha) # Вычисляем cos alpha
        self.p = getMaxFromCoords(self.sin,self.cos,coordsSet) # Получаем максимальное значение из суммы синуса умноженного на xi и косинуса умноженного на yi



    #Функция проверки на заяц/не заяц
    # Входные данные: x - координата точки, y - координата точки
    # Выходные данные: 1 - заяц; 0 - не заяц
    def getPos(self, x, y):
        d = x * self.sin + y * self.cos - self.p

        if d <=0:
            return 1
        else:
            return 0





