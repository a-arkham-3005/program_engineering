class Car: # создаем класс Car
    def __init__(self,make,model): # создаём конструктор
        self.make=make # создаём атрибут make и заносим туда значение из параметра make
        self.model=model # создаём атрибут model и заносим туда значение из параметра model
my_car=Car("Toyota","Corolla") # создаём объект my_car класса Car со значениями make="Toyota" и model="Corolla"