class DataSpoiler:
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        result=self.func(*args,**kwargs)
        if isinstance(result,str):
            result+='РиРГстыошстЫШствшотТотГШТгрмНГМнпАЕКир'
        elif isinstance(result,int):
            result+=666
        return result
@DataSpoiler
def ask_age():
    return int(input("Возраст: "))
@DataSpoiler
def ask_name():
    return input("Имя: ")
if __name__=="__main__":
    print("Вы "+ask_name()+", возраст "+str(ask_age())+" лет/год(а)")