def count_visited_houses(directions, part=1):
    visited_houses = set()
    santa_pos = [0, 0]
    robo_pos = [0, 0]
    visited_houses.add(tuple(santa_pos))

    for i, direction in enumerate(directions):
        if part == 1 or i % 2 == 0:  # Santa's turn
            move(santa_pos, direction)
            visited_houses.add(tuple(santa_pos))
        else:  # Robo-Santa's turn
            move(robo_pos, direction)
            visited_houses.add(tuple(robo_pos))

    return len(visited_houses)


def move(position, direction):
    if direction == '>':
        position[0] += 1
    elif direction == '<':
        position[0] -= 1
    elif direction == '^':
        position[1] += 1
    elif direction == 'v':
        position[1] -= 1


if __name__ == "__main__":
    with open("./day3/input.txt", "r") as file:
        directions = file.readline().strip()

    # Part 1
    print("Part 1:", count_visited_houses(directions, part=1))

    # Part 2
    print("Part 2:", count_visited_houses(directions, part=2))
