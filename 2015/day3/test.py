with open("./day3/input.txt", "r") as file:
    # part 1 
    visited_houses = set()
    x, y = 0,0
    x1, y1 = 0,0
    visited_houses.add((x,y))
    visited_houses.add((x1,y1))
    count = 2
    for dir in file.readline(): # part 1
        if count % 2 == 0:
            if dir == '>':
                x += 1
            elif dir == '<':
                x -= 1
            elif dir == '^':
                y += 1
            elif dir == 'v':
                y -= 1
            visited_houses.add((x,y))
            count += 1
        else:               # part 2
            if dir == '>':
                x1 += 1
            elif dir == '<':
                x1 -= 1
            elif dir == '^':
                y1 += 1
            elif dir == 'v':
                y1 -= 1
            count += 1
            visited_houses.add((x1,y1))
    print(len(visited_houses))


