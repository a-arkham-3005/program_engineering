with open('input.txt','a+') as f:
    f.write("\nThis is added by main.py.")
with open('input.txt','r') as f:
    print(f.readlines())