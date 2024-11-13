def fib(n):
    f1,f2=1,1
    for i in range(n):
        yield f1
        f1,f2=f2,f1+f2
if __name__=="__main__":
    fibi=fib(200)
    with open("fib.txt","w") as f:
        for i in fibi: f.write(str(i)+"\n")