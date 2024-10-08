def superset(one,two):
    if one>two: print(f"Объект {one} является чистым супермножеством")
    elif one==two: print("Множества равны")
    elif one<two: print(f"Объект {two} является чистым супермножеством")
    else: print("Супермножество не обнаружено")
if __name__=='__main__':
    superset({1,4,7,8,9},{7,8,9})
    superset({666,616},{616,666})
    superset({5,2},{1,2,5})
    superset({666,2131},{616,2132})