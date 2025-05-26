def calculate_floor_and_position(file_path):
    
    with open(file_path, "r") as file:
        line = file.readline().strip()

    # Part 1: Calculate the final floor
    floor = line.count('(') - line.count(')')
    print("Floor number is", floor)

    # Part 2: Find the position where the floor becomes -1
    current_floor = 0
    for index, char in enumerate(line, start=1):
        current_floor += 1 if char == '(' else -1
        if current_floor == -1:
            print("Position where floor becomes -1:", index)
            break

if __name__ == "__main__":
    input_file_path = "./day1/input.txt"
    calculate_floor_and_position(input_file_path)
