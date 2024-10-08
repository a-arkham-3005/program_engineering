list_1=[1,1,3,3,1]
list_2=[5,5,5,5,5,5,5]
list_3=[2,2,1,2,2,5,6,7,1,3,2,2]
set_1=set()
set_2=set()
set_3=set()
for i in set(list_1):
    for j in range(1,list_1.count(i)+1):
        if j==1: set_1.add(i)
        else: set_1.add(str(i)*j)
for i in set(list_2):
    for j in range(1,list_2.count(i)+1):
        if j==1: set_2.add(i)
        else: set_2.add(str(i)*j)
for i in set(list_3):
    for j in range(1,list_3.count(i)+1):
        if j==1: set_3.add(i)
        else: set_3.add(str(i)*j)
print(set_1,set_2,set_3,sep='\n')