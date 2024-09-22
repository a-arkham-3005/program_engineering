for i in range(11):
    print(i,".",sep="",end=" ")
    if i==0:
        i+=4
    if i==1:
        print()
        continue
    if i==2 or i==3:
        print("2 или 3")
    elif i in [4,5,6]:
        print("4,5 или 6")
    else:
        break