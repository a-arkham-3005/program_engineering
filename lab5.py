class Shape:	# создаем класс Shape
    def area(self):	# создаём метод area() для данного класса
        pass # заглушка под код
class Rectangle(Shape): # наследуем из класса Shape класс Rectangle
    def __init__(self,w,h): # создаём конструктор
        self.width=w # создаём атрибут width и заносим туда значение из параметра w
        self.height=h # создаём атрибут height и заносим туда значение из параметра h
    def area(self): # переопределяем метод area() суперкласса Shape
        return self.width*self.height # возвращает произведение значений атрибутов width и height
class Circle(Shape): # наследуем из класса Shape класс Circle
    def __init__(self,r): # создаём конструктор
        self.radius=r # создаём атрибут radius и заносим туда значение из параметра r
    def area(self): # переопределяем метод area() суперкласса Shape
        return 3.14*(self.radius**2) # возвращает произведение константы 3.14 и значения атрибута radius, возведённого в степень 2
shapes=[Circle(3),Rectangle(5,4)] # создаём в списке shapes по 1 объекту классов Circle и Rectangle со значениями соответственно radius=3 для первого объекта и width=5 и height=4 для второго объекта
print(shapes[1].area()) # вызываем метод area() для объекта shapes[1]
print(shapes[0].area()) # вызываем метод area() для объекта shapes[0]