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
    


# для использования класса нужно его поместить в переменную
# переменных может быть много
dog = animals("kas",7)
cat = animals("sit",4)
# вызов переменной
print(dog.name)
print(cat.name)
# вызов метода
dog.ran()
# способ увидеть закрытую переменную
print(cat.showYears())