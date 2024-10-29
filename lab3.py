class Car: # создаем класс Car
    def __init__(self,make,model): # создаём конструктор
        self.make=make # создаём атрибут make и заносим туда значение из параметра make
        self.model=model # создаём атрибут model и заносим туда значение из параметра model
    def drive(self): # создаём метод drive(self) для данного класса
        print(f"Driving the {self.make} {self.model}") # вывод строки по вызову метода в объекте
my_car=Car("Toyota","Corolla")  # создаём объект my_car класса Car со значениями make="Toyota" и model="Corolla"
my_car.drive()  # вызываем метод drive() для объекта my_car
class ElectricCar(Car): # наследуем из класса Car класс ElectricCar
    def __init__(self,make,model,bat_cap): # конструктор для ElectricCar
        super().__init__(make,model) # вызов конструктора родительского класса Car с параметрами make и model
        self.bat_cap=bat_cap # создаём атрибут bat_cap и заносим туда значение из параметра bat_cap
    def charge(self): # создаём метод charge(self) для данного подкласса
        print(f"Charging {self.make} {self.model} with {self.bat_cap} kWh") # вывод строки по вызову метода в объекте со всеми атрибутами объекта класса
my_electric_car=ElectricCar("Tesla","Model S",75) # создаём объект my_electric_car класса ElectricCar со значениями make="Tesla", model="Model S" и bat_cap=75
my_electric_car.drive() # вызываем метод drive() для объекта my_electric_car
my_electric_car.charge() # вызываем метод charge() для объекта my_electric_car