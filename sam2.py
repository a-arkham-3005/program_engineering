while True:
    req=input("Нужно ли вам вводить новые расходы? (0 - нет, любой другой ответ - да) ")
    if req=='0': break
    category=input("Категория расходов: ")
    number=int(input("Сумма расходов по этой категории: "))
    try:
        with open('outcomes.txt','a') as f:
            f.write(category+"\t"+str(number)+"\n")
    except FileNotFoundError:
        with open('outcomes.txt','x') as f:
            f.write(category+"\t"+str(number)+"\n")
try:
    with open('outcomes.txt','r') as f:
        print("Список расходов:")
        for i in f.readlines():
            print(i.strip("\n"))
except FileNotFoundError:
    print("Файл с расходами не найден! Запишите новые расходы.")