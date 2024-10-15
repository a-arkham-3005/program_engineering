def filter_tuple(tup,n):
    indexes=[]
    for i in range(len(tup)):
        if tup[i]==n: indexes.append(i)
    if len(indexes)==0: return tup
    out=()
    for i in range(len(indexes)):
        if i==0 and indexes[i]!=0: out+=tup[:indexes[i]]
        elif i==len(indexes)-1 and indexes[i]!=len(tup)-1: out+=tup[indexes[i]+1:]
        elif i==len(indexes)-1: break
        else: out+=tup[indexes[i]+1:indexes[i+1]]
    return out
if __name__=="__main__":
    print(filter_tuple((2,3,2,4,2),2275))
    print(filter_tuple((4,5,6,4,4,3,4),4))
    print(filter_tuple((5,6,7,4),4))