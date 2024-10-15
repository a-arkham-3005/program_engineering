numOfOffice=int(input('№ кабинета: '))
dic={
    101: {'key': 5245, 'access': True},
    102: {'key': 7463, 'access': True},
    103: {'key': 6412, 'access': True},
    104: {'key': 9051, 'access': False},
    None: {'key': None, 'access': False}
}
info=dic.get(numOfOffice)
if not info: info=dic[None]
print(info.get('key'),info.get('access'))