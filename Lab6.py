def main(**kwargs):
    for name,arr in kwargs.items():
        print(f"Numbers: {name}, mean: {avg(arr)}")

def avg(list1):
    return sum(list1)/len(list1)

if __name__=="__main__":
    main(**{'1, 5, 8, -3':[1,5,8,-3],'-3, 0, -10, 15':[-3,0,-10,15],'62, 43, -423, 300':[62,43,-423,300],'-6, -4.5, 7.3, -12':[-6,-4.5,7.3,-12]})