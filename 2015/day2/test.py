with open("./day2/input.txt", "r") as file:
    # part 1 
    total_1 = 0
    total_2 = 0
    for line in file.readlines():
        num = list(map(int, line.split("x")))
        side1, side2, side3 = num[0] * num[1], num[1] * num[2], num[2] * num[0]
        total_1 += 2 * (side1 + side2 + side3) + min(side1, side2, side3)
        num = sorted(num)
        total_2 += 2 * (num[0] + num[1]) + (num[0] * num[1] * num[2])
    print(total_1, total_2)


