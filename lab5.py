class Russian:
    @staticmethod
    def greeting():
        print("Привет")
class German:
    @staticmethod
    def greeting():
        print("Hallo")
def greet(lang):
    lang.greeting()
ivan=Russian()
greet(ivan)
hans=German()
greet(hans)