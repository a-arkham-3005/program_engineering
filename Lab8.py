from random import randint as ri
def list_maker():
    a=[ri(1,100)]*ri(3,10)
    return a
if __name__=='__main__':
    result=[]
    for i in range(ri(1,5)):
        result.append(list_maker())
    print(result)