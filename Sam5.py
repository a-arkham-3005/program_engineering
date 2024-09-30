from module import heron

if __name__=="__main__":
    a=int(input("Длина 1 стороны треугольника: "))
    b=int(input("Длина 2 стороны треугольника: "))
    c=int(input("Длина 3 стороны треугольника: "))
    print(f"Площадь такого треугольника равна {heron(a,b,c)}")