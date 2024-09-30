from random import randint

def dice():
    num=randint(1,6)
    if num==5 or num==6: print(num,"Вы победили",sep='\n')
    elif num==3 or num==4:
        print(num)
        dice()
    else: print(num,"Вы проиграли",sep='\n')

if __name__=="__main__":
    dice()