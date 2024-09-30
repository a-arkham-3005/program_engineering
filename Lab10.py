global result

def rect(a,b):
    global result
    result=a*b

def tri(a,h):
    global result
    result=a*h/2

fig=input("П - прямоугольник, Т - треугольник? ")

if fig=='П':
    rect(float(input("Ширина? ")),float(input("Высота? ")))
elif fig=='Т':
    tri(float(input("Основание? ")), float(input("Высота? ")))

print(f"Площадь равна {result}")