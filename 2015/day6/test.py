import time

def count_lit_lights(grid):
    count = 0
    for row in grid:
        count += sum(row)
    return count

with open("./day6/input.txt", "r") as file:
    instructions = file.readlines()
    # Initialize the grid with all lights turned off
    grid = [[False] * 1000 for _ in range(1000)]
    grid_2 = [[0] * 1000 for _ in range(1000)]

    for instruction in instructions:
        parts = instruction.split()
        start_x, start_y = map(int, parts[-3].split(','))
        end_x, end_y = map(int, parts[-1].split(','))
        
        # part 1``
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if 'toggle' in instruction:
                    grid[x][y] = not grid[x][y]
                    grid_2[x][y] += 2
                elif 'turn on' in instruction:
                    grid[x][y] = True
                    grid_2[x][y] += 1
                elif 'turn off' in instruction:
                    grid[x][y] = False
                    if grid_2[x][y] > 0:
                        grid_2[x][y] -= 1
        

# Calculate the count of lit lights
start = time.time()
lit_count = count_lit_lights(grid)
brightness = count_lit_lights(grid_2)
print("Number of lit lights:", lit_count, "brightness:", brightness, (time.time() - start))
start = time.time()
lit_count = sum([sum(sum(x) for x in grid)])
lit_count = sum([sum(sum(x) for x in grid)])
print("Number of lit lights:", lit_count, "brightness:", brightness, (time.time() - start))