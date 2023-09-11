grid = []
for line in open("day18/input.txt", "r").readlines():
    grid.append([light for light in line.strip()])


def find_neighbors(grid):
    """Finds the neighbors of each value in the grid.

    Args:
        grid: A 2D list of integers.

    Returns:
        A 2D list of lists of integers, where each inner list contains the neighbors of
        the corresponding value in the input grid.
    """
    neighbors = []
    for i in range(len(grid)):
        neighbor_row = []
        for j in range(len(grid[0])):
            neighbor_list = []
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and (i + di, j + dj) != (i, j):
                        neighbor_list.append(grid[i + di][j + dj])
            neighbor_row.append(neighbor_list)
        neighbors.append(neighbor_row)
    return neighbors

for i in range(0, 100):
    neighbors = find_neighbors(grid)
    i = 0
    j = 0
    for neighbor in neighbors:
        for row in neighbor:
            # part 1
            if grid[i][j] and not 2 <= row.count("#") <= 3:
                grid[i][j] = grid[i][j].replace("#", ".")
            elif row.count("#") == 3:
                grid[i][j] = grid[i][j].replace(".", "#")
            j += 1
        j = 0
        i += 1
    i = 0

    # part 2
    grid[0][0] = grid[0][0].replace(".", "#")
    grid[0][99] = grid[0][99].replace(".", "#")
    grid[99][0] = grid[99][0].replace(".", "#")
    grid[99][99] = grid[99][99].replace(".", "#")

print("Total number lights in on state after 100 steps of operation:", 
        sum([row.count("#") for row in grid]))