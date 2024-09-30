def main(**kwargs):
    for n in kwargs:
        print(f"The value of {n} is {kwargs[n]}")
    for n in kwargs.items():
        print(f"{n[0]}={n[1]}")

if __name__=="__main__":
    main(one=1,two=2,three=3)
    print()
    main(**{'class':'main','lalala':'zhuzhuzhu'})