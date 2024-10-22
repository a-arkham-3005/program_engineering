data=''
file_open=False
name1=input("Путь до файла: ")
name2=input("Куда копировать? ")
try:
    with open(name1,'r',encoding='utf-8') as f:
        data=f.read()
        file_open=True
except FileNotFoundError:
    print("Файл не найден!")
if file_open:
    try:
        with open(name2, 'x', encoding='windows-1251') as f:
            f.write(data)
    except FileExistsError:
        with open(name2, 'w', encoding='windows-1251') as f:
            f.write(data)