class Car: # создаем класс Car
    def __init__(self,make,model): # создаём конструктор
        self.make=make # создаём атрибут make и заносим туда значение из параметра make
        self.model=model # создаём атрибут model и заносим туда значение из параметра model
    def drive(self): # создаём метод drive(self) для данного класса
        print(f"Driving the {self.make} {self.model}") # вывод строки по вызову метода в объекте
my_car=Car("Toyota","Corolla") # создаём объект my_car класса Car со значениями make="Toyota" и model="Corolla"
my_car.drive() # вызываем метод drive() для объекта my_car