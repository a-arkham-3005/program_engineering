def rep(list):
    list[0],list[-1]=list[-1],list[0]
    return list
print(rep(['q','w','e','r','t','z']))