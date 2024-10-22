def longword(fil):
    with open(fil,encoding='utf-8') as f:
        wordz=f.read().split()
        maxLen=len(max(wordz,key=len))
        sought=[]
        for w in wordz:
            if len(w)==maxLen: sought.append(w)
        if len(sought)==1: return sought[0]
        return sought
print(longword('input.txt'))