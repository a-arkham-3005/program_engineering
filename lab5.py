def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm,int): return tpl
    return tuple(sorted(tpl))
if __name__=="__main__":
    print(tuple_sort((3,6,2,6,1,7,9,4,2,8)))
    print(tuple_sort(("O",12,5,1,5,0,1,4)))