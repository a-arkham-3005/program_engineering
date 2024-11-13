def sum():
    try:
        inp = int(input())
        print(2 + inp)
    except ValueError:
        print("Неподходящий тип данных, ожидалось число")
if __name__=="__main__":
    sum()