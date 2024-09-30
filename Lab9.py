from datetime import date, timedelta as td

def num_to_weekday(num):
    if num==0: return 'понедельник'
    elif num==1: return 'вторник'
    elif num==2: return 'среда'
    elif num==3: return 'четверг'
    elif num==4: return 'пятница'
    elif num==5: return 'суббота'
    else: return 'воскресенье'

def main():
    today=date.today()
    print(
        f"Сегодня {num_to_weekday(today.weekday())}, {today}"
    )
    n=int(input("Введите количество дней: "))
    ndays=today+td(days=n)
    print(
        f"Через {n} дней будет {num_to_weekday(ndays.weekday())}, {ndays}"
    )

if __name__=="__main__":
    main()