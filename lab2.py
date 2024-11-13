def check(fun):
    def out(*args):
        name,age=args[0],args[1]
        if age<0 or age>130:
            age='Недопустимый возраст'
        fun(name,age)
    return out
@check
def persInfo(n,a):
    print(f"Name: {n}, Age: {a}")
if __name__=="__main__":
    persInfo('Alex',36)
    persInfo('John',-21)
    persInfo('Michael',321)