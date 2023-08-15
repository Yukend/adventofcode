with open("./day1/input.txt", "r") as file:
    # part 1 
    line = file.readline()
    print("Floor number is", line.strip().count('(') - line.strip().count(')')) # ans = 74
    # part 2
    index = 0
    floor = 0
    for char in line:
        index += 1
        floor = floor + 1 if char == '(' else floor - 1
        if floor == -1:
            print(index) # ans = 1795
            break


