with open('article.txt','r') as f:
    words=f.read().split()
    numOfWords=len(words)
    maxWordCount=max([words.count(i) for i in words])
    maxWord=''
    for i in words:
        if words.count(i)==maxWordCount: maxWord=i
    print(f"Самое часто встречаемое слово в статье - {maxWord}, встречается {maxWordCount} раз(а). Всего слов - {numOfWords}.")