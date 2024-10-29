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