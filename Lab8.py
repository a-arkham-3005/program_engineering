from math import sin, cos, sqrt

def main(num):
    print(f"sin({num})={sin(num)}, cos({num})={cos(num)}, sqrt({num})={sqrt(num)}")

if __name__=="__main__":
    main(float(input("Введите число: ")))