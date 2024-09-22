string="Слава КПСС"
value=input("Введите букву. ")
for f in string:
    if value==f:
        index=string.find(value)
        print(f"Буква '{value}' есть в строке под номером {index+1}")
        break
else:
    print(f"Буквы '{value}' нет в строке")