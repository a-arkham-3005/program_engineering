class Icecream:
    def __init__(self,ingredient=None):
        if isinstance(ingredient,str): self.ingredient=ingredient
        else: self.ingredient=None
    def composition(self):
        if self.ingredient:
            print(f"Мороженое с: {self.ingredient}")
        else: print("Обычное мороженое")
ic=Icecream()
ic2=Icecream('Шоколадом')
ic3=Icecream(666)
ic.composition()
ic2.composition()
ic3.composition()