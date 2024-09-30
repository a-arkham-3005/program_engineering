def toot(*args):
    summ=0
    for i in args: summ+=abs(i)
    return summ

if __name__=="__main__":
    print(toot(12,-32,5,-45,34,-34,64,32,2,81))