nums=[-13, -7, 0, 2, 5, 10, 23]
value=int(input("Введите число: "))
if value in nums:
    if value%2==0:
        print("Число есть в массиве, оно чётное")
    else:
        print("Число есть в массиве, оно нечётное")
else:
    print(f"Числа {value} нет в массиве")