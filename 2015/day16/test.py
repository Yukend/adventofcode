components = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}
for line in open("day16/input.txt", "r").readlines():
    line = line.rstrip().replace(",", "").split(" ")
    find_sue = [(line[2],line[3]), (line[4],line[5]), (line[6],line[7])]
    # part 1 run after commend part 2
    # if all(int(value) == components[item[:-1]] for item, value in find_sue):
    #     print(line[1])
    #     break

    # part 2 run after commend part 1
    find_sue_2 = []
    for item, value in find_sue:
        if item[:-1] in ["cats", "trees"] and int(value) >= components[item[:-1]]:
            find_sue_2.append(True)
        elif item[:-1] in ["pomeranians" , "goldfish"] and int(value) <= components[item[:-1]]:
            find_sue_2.append(True)
        elif int(value) == components[item[:-1]]:
            find_sue_2.append(True)
    if line[1] != "213:" and sum(find_sue_2) == 3:
        print(line[1])
        break
