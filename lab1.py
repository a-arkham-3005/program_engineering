class Eduard:
    __slots__=['name']
    def __init__(self,name):
        if name=='Эдуард':
            self.name=f"Да, я {name}"
        else:
            self.name=f"Я не {name}, а Эдуард"
person1=Eduard("Пётр")
person2=Eduard("Эдуард")
print(person1.name)
print(person2.name)
person2.surname='Шевнин'