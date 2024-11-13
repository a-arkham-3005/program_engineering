class NumTooLongFor32bitError(Exception):
    def __init__(self,err):
        super().__init__(err)
def fibo(n):
    fib1,fib2=1,1
    for i in range(2,n+1):
        fib1,fib2=fib2,fib1+fib2
        if fib2>2147483647:
            raise NumTooLongFor32bitError("Fibonacci number #"+str(n)+" is too long to fit in 32-bit integer")
    return fib2
def fact(n):
    mul=1
    for i in range(2,n+1):
        mul*=i
        if mul>2147483647:
            raise NumTooLongFor32bitError("Factorial of "+str(n)+" is too long to fit in 32-bit integer")
    return mul
if __name__=="__main__":
    try:
        print(fact(13))
    except NumTooLongFor32bitError as e:
        print(e)
    finally:
        try:
            print(fibo(45))
        except NumTooLongFor32bitError as e:
            print(e)