import math

def area(a,b,c):
    p=(a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

if __name__=="__main__":
    one=[12, 25, 3, 48, 71]
    two=[5, 18, 40, 62, 98]
    three=[4, 21, 37, 56, 84]
    print("Площадь треугольника из минимальных элементов:",area(min(one),min(two),min(three)))
    print("Площадь треугольника из максимальных элементов:",area(max(one),max(two),max(three)))