def between1stand2nd(tup,n):
    inds=[]
    for i in range(len(tup)):
        if tup[i]==n: inds.append(i)
        if len(inds)==2: break
    if len(inds)==0: return ()
    elif len(inds)==1: return tup[inds[0]:]
    else: return tup[inds[0]:inds[1]+1]
if __name__=="__main__":
    print(between1stand2nd((1,2,3),8))
    print(between1stand2nd((1,8,3,4,8,8,9,2),8))
    print(between1stand2nd((1,2,8,5,1,2,9),8))