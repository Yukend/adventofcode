with open("./day1/input.txt", "r") as file:
    # part 1 
    line = file.readline()
    print("Floor number is", 
        line.strip().count('(') - 
        line.strip().count(')')) 
    # part 2
    index = 0
    floor = 0
    for char in line:
        index += 1
        floor = floor + 1 if char == '(' else floor - 1
        if floor == -1:
            break


