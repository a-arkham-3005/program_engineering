class FileEmptyError(Exception):
    def __init__(self):
        super().__init__('File is empty!')
try:
    with open('full.txt','r') as f:
        a=f.read()
        if not a:
            raise FileEmptyError()
        else:
            print(a)
except FileEmptyError as err:
    print(err)