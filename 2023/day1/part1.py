import regex as re

count = 0
for i in open("input.txt", "r").readlines():
    value_list = re.findall("[0-9]", i)
    if len(value_list) == 1:
        count += int(value_list[0] + value_list[0])
    else:
        count += int(value_list[0] + value_list[-1])
print(count)