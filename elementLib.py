# Класс нейрона

import numpy # испортируем сложные вычисления
import creations

# Функция для рассчета максимального значения для всех пробных точек
# Вход: sin угла, cos угла, набор пробных точек
# Максимальное значение из суммы синуса умноженного на xi и косинуса умноженного на yi



# Основной класс нейрона
class DecisiveFunction:




    # Определяющая функция
    # Вход: номер нейрона j, набор пробных точек в формате: [(x1,y1),(x2,y2),...]
    def __init__(self, id, coordsSet):
        self.j = id # Присваиваем j
        self.alpha = 2* numpy.pi /  360  * id # Вычисляем угол alpha (каким из углов будет этот нейрон )


        self.sin = numpy.sin(self.alpha) # Вычисляем sin alpha
        self.cos = numpy.cos(self.alpha) # Вычисляем cos alpha


        self.p= max(map(lambda x: x[0]*self.cos+x[1]*self.sin,coordsSet)) # Получаем максимальное значение из суммы синуса умноженного на xi и косинуса умноженного на yi

        #creations.creating_line(self.sin, self.cos,res[id][0],res[id][1],color="green", width=4)
        # рисуем отделяющую линию
        #creations.creating_line(self.p,self.sin, self.cos,color="black")




    #Функция проверки на заяц/не заяц
    # Входные данные: x - координата точки, y - координата точки
    # Выходные данные: 1 - заяц; 0 - не заяц
    def getPos(self, x, y):
        d = x * self.cos + y * self.sin - self.p

        #рисуем вектор (если функция перестроена)
        #creations.creating_line(self.sin, self.cos,x,y,color="orange")


        if d <=0:
            return 0
        else:
            return 1





