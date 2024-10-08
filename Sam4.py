one=[2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two=[4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three=[5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
for i in range(one.count(2)): one.remove(2)
for i in range(two.count(2)): two.remove(2)
for i in range(three.count(2)): three.remove(2)
for i in range(len(one)):
    if one[i]==3: one[i]=4
for i in range(len(two)):
    if two[i]==3: two[i]=4
for i in range(len(three)):
    if three[i]==3: three[i]=4
print(one,two,three,sep='\n')