def tuple_filter(tup,v):
    if not tup.__contains__(v): return tup
    else:
        ind=tup.index(v)
        if ind==0: return tup[1:]
        elif ind==len(tup)-1: return tup[:-1]
        else: return tup[0:ind]+tup[ind+1:]

if __name__=="__main__":
    print(tuple_filter((1,2,3),1))
    print(tuple_filter((1,2,3,1,2,3,4,5,2,3,4,2,4,2), 3))
    print(tuple_filter((2,4,6,6,4,2), 9))