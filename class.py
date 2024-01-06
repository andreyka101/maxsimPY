# тело класса
class animals():
    # создание переменных
    sight = "добрый"
    # функция конструктор обязательно нужно в качестве первой переменной передавать self
    def __init__(self , a = "kas",s = 1):
        # создание или изменение переменных в методах , конструкторе
        # пишем в начале  self
        self.name = a
        # закрытая переменная
        self.__private_years = s
        self.__private_years *= 10
    # методы им нужно обязательно в качестве первой переменной передавать self
    # работают как функции
    def ran(self):
        print(self.name+" ran")
    def showYears(self):
        return self.__private_years
    def retALL (self):
        return [self.name, self.__private_years]
    


# для использования класса нужно его поместить в переменную
# переменных может быть много
dog = animals("kas",7)
cat = animals("sit",4)
# вызов переменной
# print(dog.name)
# print(cat.name)
# вызов метода
# dog.ran()
# способ увидеть закрытую переменную
# print(cat.showYears())


# dz class
# номер 1
# Создать класс, описывающий автомобиль (производитель, 
# модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации об автомобиле.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.



# урок 2 

class transport():
    ani = animals()

    def __init__(self, name : str, speed : int , numberPassengers : int , machineWeight : int):
        """.metod(name = str , speed = num , numberPassengers = num , machineWeight = num)"""
        self.name = name
        self.speed = speed
        self.numberPassengers = numberPassengers
        self.machineWeight = machineWeight


    def timeTravel(self, distance):
        """aniani"""
        return distance/(self.speed-self.machineWeight) , "час"
    def wer (self):
        print(self.speed)
    

# создаём класс Cаr который наследуется от класса trаnsроrt
class Car(transport):
    # обычный конструктор init
    def __init__(self, name: str, speed: int, numberPassengers: int, machineWeight: int , petrol : int):
        # с помощью super наследуем все переменные и методы от класса родителя 
        super().__init__(name, speed, numberPassengers, machineWeight)
        # создаём новую переменную
        self.petrol = petrol
    # создаём новый метод
    def maximumDistance(self):
        return self.petrol * self.speed
    # изменяем метод родителя
    def timeTravel(self, distance):
        """aniani"""
        



bike = transport("my bike", 20 , 1 , 3)
# print(bike.timeTravel(100))
# bike.ani.ran()

carRed = Car("my car" , 300 , 2 , 50 , 6)
# print(carRed.timeTravel(5000))
# print(carRed.maximumDistance())


# домашнее задание урока 2
# номер 1
# создать класс колькулятор 
# в конструкторе нужно в писать 2 числа
# создать 4 метода: умножение , деление , сумма , вычитание
# создать метод для добавления числа (его можно вызвать много раз и подучить много чисел)

# урок 3  -------------------------------------------------------


# class drink():
#     ...
class coffee():
    sight = "добрый"
    def __init__(self , a = "kas",s = 1):
        self.name = a
        self.__private_years = s
        self.__private_years *= 10
    def ran(self):
        print(self.name+" ran")

class tea():
    sight = "добрый"
    def __init__(self , a = "kas",s = 1):
        self.name = a
        self.__private_years = s
        self.__private_years *= 10
    def ran(self):
        print(self.name+" ran")

class cocoa():
    sight = "добрый"
    def __init__(self , a = "kas",s = 1):
        self.name = a
        self.__private_years = s
        self.__private_years *= 10
    def ran(self):
        print(self.name+" ran")
    
class drink ():
    coffee = coffee()
    tea = tea()
    cocoa = cocoa()
        

# afternoon = drink().tea
# afternoon.ran()


# домашнее задание урока 3
# номер 1
# сделать класс editor который принимает переменную (название txt файла)
# у этого класса сделать методы 
# 1. conclusion - вывод из txt файла
# 2. change - изменить текст в txt файле
# 3. add - дописать текст в txt файл
# не забудь воспользоваться методом .close() который закрывает файл

