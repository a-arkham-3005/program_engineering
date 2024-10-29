class Car: # создаем класс Car
    def __init__(self,make,model): # создаём конструктор
        self._make=make # создаём protected атрибут make и заносим туда значение из параметра make
        self.__model=model # создаём private атрибут model и заносим туда значение из параметра model
    def drive(self): # создаём метод drive(self) для данного класса
        print(f"Driving the {self._make} {self.__model}") # вывод строки по вызову метода в объекте
my_car=Car("Toyota","Corolla") # создаём объект my_car класса Car со значениями make="Toyota" и model="Corolla"
print(my_car._make) # вывод protected-атрибута
# print(my_car.__model) # private-атрибуты нельзя прочитать извне - компилятор их не увидит 
my_car.drive() # вызываем метод drive() для объекта my_car