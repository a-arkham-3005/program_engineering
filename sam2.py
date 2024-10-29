class AppleComputer:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def info(self):
        print(f"This is {self.name}, built in {self.year}")
apple2=AppleComputer("Apple II",1977)
apple2.info()