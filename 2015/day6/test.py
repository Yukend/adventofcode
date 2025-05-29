def parse_instruction(instruction):
    """Parses an instruction and returns the action and coordinates."""
    parts = instruction.split()
    if 'toggle' in instruction:
        action = 'toggle'
        start_coords = parts[1]
        end_coords = parts[3]
    else:
        action = 'turn on' if 'turn on' in instruction else 'turn off'
        start_coords = parts[2]
        end_coords = parts[4]
    start_x, start_y = map(int, start_coords.split(','))
    end_x, end_y = map(int, end_coords.split(','))
    return action, start_x, start_y, end_x, end_y

def apply_instruction(grid, grid_2, action, start_x, start_y, end_x, end_y):
    """Applies the given instruction to both grids."""
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == 'toggle':
                grid[x][y] = not grid[x][y]
                grid_2[x][y] += 2
            elif action == 'turn on':
                grid[x][y] = True
                grid_2[x][y] += 1
            elif action == 'turn off':
                grid[x][y] = False
                grid_2[x][y] = max(0, grid_2[x][y] - 1)

def main():
    with open("./day6/input.txt", "r") as file:
        instructions = file.readlines()

    # Initialize the grids
    grid = [[False] * 1000 for _ in range(1000)]
    grid_2 = [[0] * 1000 for _ in range(1000)]

    # Process each instruction
    for instruction in instructions:
        action, start_x, start_y, end_x, end_y = parse_instruction(instruction)
        apply_instruction(grid, grid_2, action, start_x, start_y, end_x, end_y)

    lit_count = sum(sum(row) for row in grid)
    brightness = sum(sum(row) for row in grid_2)

    print(f"Number of lit lights: {lit_count}, Brightness: {brightness}")
    

if __name__ == "__main__":
    main()