# Тема 8. Введение в ООП.

Отчёт по теме №8 выполнил:

- Хайрутдинов Игорь Юрьевич
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------- | ------- | ------- |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

Работу проверил:

- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами Производитель и Модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car: # создаем класс Car
    def __init__(self,make,model): # создаём конструктор
        self.make=make # создаём атрибут make и заносим туда значение из параметра make
        self.model=model # создаём атрибут model и заносим туда значение из параметра model
my_car=Car("Toyota","Corolla") # создаём объект my_car класса Car со значениями make="Toyota" и model="Corolla"
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/lab1.png)

## Выводы

Результат выполнения программы представлен на скриншоте выше.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car: # создаем класс Car
    def __init__(self,make,model): # создаём конструктор
        self.make=make # создаём атрибут make и заносим туда значение из параметра make
        self.model=model # создаём атрибут model и заносим туда значение из параметра model
    def drive(self): # создаём метод drive(self) для данного класса
        print(f"Driving the {self.make} {self.model}") # вывод строки по вызову метода в объекте
my_car=Car("Toyota","Corolla") # создаём объект my_car класса Car со значениями make="Toyota" и model="Corolla"
my_car.drive() # вызываем метод drive() для объекта my_car
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/lab2.png)

## Выводы

Результаты выполнения программ представлены на скриншотах выше.

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом Ёмкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
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
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/lab3.png)

## Выводы

Результат выполнения программы представлен на скриншоте выше.

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
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
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/lab4.png)

## Выводы

Результат выполнения программы представлен на скриншоте выше.

## Лабораторная работа №5
### Реализуйте полиморфизм, создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
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
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/lab5.png)

## Выводы

Результат выполнения программы представлен на скриншоте выше.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class AppleComputer:
    def __init__(self,name):
        self.name=name
apple2=AppleComputer("Apple II")
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/sam1.png)

## Выводы

Данный код содержит класс AppleComputer. Он инициализируется в первой строке кода после ключевого слова class. В нём (классе) содержится функция `__init__(self,name)`, которая служит конструктором функции. При создании объекта вызывается именно она. Ключевое слово self указывает на экземпляр класса (объект), name же здесь - параметр функции. Далее устанавливается атрибут name в объекте (на что указывает self до названия атрибута) со значением, равным параметру функции name. Данный код всего-лишь создаёт объект класса AppleComputer с названием apple2 со значением атрибута name, равным "Apple II". На консоль ничего не выводится.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class AppleComputer:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def info(self):
        print(f"This is {self.name}, built in {self.year}")
apple2=AppleComputer("Apple II",1977)
apple2.info()
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/sam2.png)

## Выводы

Данный код содержит всё тот же класс AppleComputer. В конструкторе добавлен параметр year для функции, а также добавлен атрибут year. За конструктором идёт метод info(self), указывающий, опять же, на то, что эта функция выполняется при каком-либо объекте. Этот метод выводит на экран строку `This is {self.name}, built in {self.year}`, выводя значения обоих атрибутов name и year в консоль для определённого объекта. К объекту apple2 добавлен атрибут year со значением 1977, затем вызывается метод info() в рамках этого объекта. Результат выполнения программы представлен на скриншоте выше.

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class AppleComputer:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def info(self):
        print(f"This is {self.name}, built in {self.year}")
class MacBook(AppleComputer):
    def __init__(self,model,year,battery):
        super().__init__(model,year)
        self.battery=battery
    def info(self):
        print(f"This is {self.name}, built in {self.year} with battery capacity {self.battery} mAh")
apple2=AppleComputer("Apple II",1977)
apple2.info()
mbp2018=MacBook("MacBook Pro",2018,7336)
mbp2018.info()
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/sam3.png)

## Выводы

Данный код содержит всё тот же класс AppleComputer с теми же атрибутами и методами. В этом коде присутствует класс MacBook, унаследдованный от AppleComputer, о чём говорит название родительского класса в скобках после названия дочернего. Конструктор этого класса принимает параметры model, year и battery. С первыми двумя параметрами вызывается конструктор родительского класса по ключевому слову super(). Значение третьего же параметра переходит в атрибут battery, принадлежащий исключительно классу MacBook, но не AppleComputer. Строка вывода для переопределённого метода init() изменена на "This is {self.name}, built in {self.year} with battery capacity {self.battery} mAh", с выводом значений соответствующих атрибутов в консоль. Создание объекта apple2 и вызов его метода info() всё так же осуществляются. Но этот код также создаёт объект mbp2018 класса MacBook с параметрами "MacBook Pro", 2018 и 7336, передаваемых конструктору. У этого объекта также вызывается функция info(). Результат выполнения программы представлен на скриншоте выше.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class AppleComputer:
    def __init__(self,name,year):
        self.name=name
        self._year=year # protected
    def info(self):
        print(f"This is {self.name}, built in {self._year}")
class MacBook(AppleComputer):
    def __init__(self,model,year,battery):
        super().__init__(model,year)
        self.__battery=battery # private
    def info(self):
        print(f"This is {self.name}, built in {self._year} with battery capacity {self.__battery} mAh")
apple2=AppleComputer("Apple II",1977)
apple2.info()
mbp2018=MacBook("MacBook Pro",2018,7336)
mbp2018.info()
print(mbp2018._year)
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/sam4.png)

## Выводы

Данный код содержит всё те же классы AppleComputer с теми же атрибутами и методами. Но в этот раз атрибут year классов AppleComputer, а соответственно и MacBook, объявлен как защищённый, о чём говорит один символ нижнего подчёркивания перед названием. Защищённые атрибуты не могут быть прочитаны или записаны за пределами выполняемой программы (за исключением наследуемых классов), но могут быть использованы повсеместно внутри программы. Также атрибут battery в классе MacBook объявлен как частный (private). Это означает, что атрибут доступен только внутри самого класса MacBook. Объекты apple2 и mbp2018 также инициализируются, и от каждого из них выполняется метод info(). После этого программа пытается попасть к защищённому атрибуту year объекта mbp2018, и это получается успешно - программа, в которой инициализируются классы, может видеть защищённые атрибуты напрямую. При попытке сделать то же самое с атрибутом battery вызывается исключение - программа не видит частные атрибуты объектов напрямую. Результат выполнения программы представлен на скриншоте выше.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class AppleDevice:
    def info(self):
        pass
class IPhone(AppleDevice):
    def __init__(self,model,year,chrg,home):
        self.name="iPhone "+model
        self.year=year
        self.charger=chrg
        self.home=home
    def info(self):
        if self.home:
            print(f"This is {self.name} of year {self.year}. It has home button and {self.charger} port.")
        else:
            print(f"This is {self.name} of year {self.year}. It doesn't have home button and has {self.charger} port.")
class MacBook(AppleDevice):
    def __init__(self,model,year,usba,touchbar,silicon):
        self.name="MacBook "+model
        self.year=year
        self.usbA=usba
        self.touchbar=touchbar
        self.silicon=silicon
    def info(self):
        stri="This is "+self.name+" of year "+str(self.year)+". "
        if self.usbA: stri+="It still has old USB-A ports. "
        else: stri+="It only has Thunderbolt ports and no USB-A. "
        if self.touchbar: stri+="It has a TouchBar. "
        else: stri+="It doesn't have TouchBar. "
        if self.silicon: stri+="It's based on Apple Silicon."
        else: stri+="It's based on Intel processor."
        print(stri)

ip7plus=IPhone("7 Plus",2016,"Lightning",True)
ip15pm=IPhone("15 Pro Max",2023,"Type-C",False)
mbp2013=MacBook("Pro",2013,True,False,False)
mbpM1=MacBook("Pro",2021,False,True,True)
mbaM3=MacBook("Air",2023,False,False,True)
ip7plus.info()
ip15pm.info()
mbp2013.info()
mbpM1.info()
mbaM3.info()
```
### Результат
![скрин](https://github.com/a-arkham-3005/program_engineering/blob/Тема_8/screens/sam5.png)

## Выводы

Данная программа содержит три класса: AppleDevice, IPhone и MacBook, причём два последних унаследованы от первого. В первом из классов нет конструктора, но есть метод info(), содержащий заглушку - ключевое слово pass. В остальных классах есть реализация этого метода, а также конструктор - у каждого свой. Например, класс IPhone принимает параметры, записываемые в атрибуты name, year, charger и home. Метод info() у этого класса выводит значения первых трёх атрибутов в строку, последний же, home, проверяется через if на логическую составляющую (True или False). Если home=True, то выводится строка `This is {self.name} of year {self.year}. It has home button and {self.charger} port.`, иначе строка `This is {self.name} of year {self.year}. It doesn't have home button and has {self.charger} port.`. В классе же MacBook атрибутов больше, а в строку выводятся только name и year, остальные проверяются по логической составляющей каждого из них для конкатенации (добавления) в строку `"This is "+self.name+" of year "+str(self.year)+". "` строк с дополнительной информацией, затем готовая строка выводится на экран целиком. После инициализации классов и методов, код начинает инициализацию объектов ip7plus, ip15pm (класса IPhone), mbp2013, mbpM1 и mbaM3 (класса MacBook) с соответствующими этим устройствам характеристиками, найденными в Интернете, затем от каждого из этих 5 объектов вызывается метод info(). Результат выполнения программы представлен на скриншоте выше.

## Общие выводы по теме

В рамках данной темы мы изучили основы объектно-ориентированного программирования на языке Python. Мы научились:

1. Инициализировать классы в коде;

2. Создавать конструтор - метод `__init__(self)`, создавать атрибуты объектов;

3. Создавать методы для объектов класса;

4. Наследовать классы, переопределять методы и вызывать методы родительского класса - принцип наследования;

5. Защищать данные атрибутов от внешнего доступа через параметры доступа protected и private в названии атрибута (через определённое количество нижних подчёркиваний перед названием) - принцип инкапсуляции;

6. Создавать классы-интерфейсы с заглушками методов для реализации принципа полиморфизма.
