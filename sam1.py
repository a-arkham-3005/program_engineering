import time
def runtime(func):
    def wrapper(*args):
        start=time.time()
        result=func(*args)
        end=time.time()
        run_time=end-start
        print('      Function runtime:',run_time,'s')
        return result
    return wrapper
@runtime
def fibonacci():
    fib1=fib2=1
    for i in range(2,200):
        fib1,fib2=fib2,fib1+fib2
    print(fib2,end=' ')
if __name__=="__main__":
    fibonacci()