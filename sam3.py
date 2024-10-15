def dict_builder(line):
    nums = line.split(" ")
    for el in range(len(nums)):
        nums[el] = int(nums[el])
    dic = {}
    for i in nums:
        if not dic.__contains__(i):
            dic.update({i: 1})
        else:
            dic[i] += 1
    temp = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    dic = dict(temp[:3])
    return dic
if __name__=="__main__":
    line = input("Введите числа через пробел. ")
    print(dict_builder(line))