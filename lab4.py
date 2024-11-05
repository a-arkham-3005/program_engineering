class Mammal:
    className='Mammal'
class Dog(Mammal):
    species='Canine'
    sounds='woof'
class Cat(Mammal):
    species='Feline'
    sounds='miau'
dog=Dog()
print(f"Dog is a {dog.className}, they say {dog.sounds}")
cat=Cat()
print(f"Cat is a {cat.className}, they say {cat.sounds}")