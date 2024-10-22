import re
with open('input.txt','r') as f:
    banned=f.readline().strip().split()
    censor=['*'*len(i) for i in banned]
    sentence="Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    for i in range(len(banned)):
        sentence=re.sub(banned[i],censor[i],sentence,flags=re.IGNORECASE)
    print(sentence)