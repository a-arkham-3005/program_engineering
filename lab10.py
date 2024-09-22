flag=False
nums=[-22, -14, -7, 0, 4, 12]
for i in nums:
    if i%2==1: flag=True
if flag:
    print('Найдено нечётное число')
else:
    print('Все числа чётные')