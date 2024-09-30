def mean(*args):
    result=0
    count=0
    for i in args:
        result+=i
        count+=1
    return result/count

if __name__=="__main__":
    print(mean(2,-4,32,3,-21,3,-4,2,-3,4,12,3))