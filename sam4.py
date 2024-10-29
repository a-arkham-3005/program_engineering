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