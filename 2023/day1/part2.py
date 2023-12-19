import regex as re


count = 0
re_l = {"one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
for i in open("input.txt", "r").readlines():
    over_lap_map = {"oneight": "oneeight", "twone": "twoone", "threeight": "threeeight",
                    "fiveight": "fiveeight", "sevenine": "sevennine", 
                    "eightwo": "eighttwo", "nineight": "nineeight"}
    for k, v in over_lap_map.items():
        if k in i:
            i = i.replace(k, v)
    val_l = re.findall("one|two|three|four|five|six|seven|eight|nine|\d", i)
    if len(val_l) == 1:
        count += int(re_l[val_l[0]] + re_l[val_l[0]]
                    ) if val_l[0] in re_l else int(val_l[0] + val_l[0])
    else:
        val_1 = re_l[val_l[0]] if val_l[0] in re_l else val_l[0]
        val_2 = re_l[val_l[-1]] if val_l[-1] in re_l else val_l[-1]
        count += int(val_1 + val_2)
print(count)
