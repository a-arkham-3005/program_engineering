input_data=input("Введите числа через пробел: ")
inp_l=input_data.split(" ")
for el in range(len(inp_l)):
    inp_l[el]=int(inp_l[el])
inp_t=tuple(inp_l)
print(inp_l,inp_t,sep='\n')