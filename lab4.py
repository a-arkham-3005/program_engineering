def personal_info(name,age,company='NONAME'):
    print(f"Имя: {name}, Возраст: {age}, компания: {company}")
tom=("Григорий",22)
personal_info(*tom)
bob=("Георгий",41,"Яндекс")
personal_info(*bob)