import os
def print_docs(directory):
    listi=os.walk(directory)
    for i in listi:
        print(f"Папка {i[0]} содержит:")
        print(f"Папки: {",".join([j for j in i[1]])}")
        print(f"Файлы: {",".join([j for j in i[2]])}")
        print('-'*40)
if __name__=="__main__":
    print_docs(os.environ['userprofile']+'\\Pictures')