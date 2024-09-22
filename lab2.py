check=int(input("Введите число: "))
if check<0:
    print('Меньше 0')
elif 0<check<10:
    print('Больше 0 и меньше 10')
else:
    print('Больше 10')