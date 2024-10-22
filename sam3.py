with open('input.txt','r') as f:
    lines=f.readlines()
    numOfLines=len(lines)
    numOfWords=sum([len(i.split()) for i in lines])
    numOfLetters=0
    letters=[chr(i) for i in range(ord('A'),ord('Z')+1)]+[chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in lines:
        for j in i.split():
            for k in j:
                if k in letters: numOfLetters+=1
	print("Input file contains:")
    print(numOfLetters,"letters")
    print(numOfWords,"words")
    print(numOfLines,"lines")