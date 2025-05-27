# Path to the input file
input_file_path = "./day2/input.txt"

# Initialize totals for part 1 and part 2
total_wrapping_paper = 0
total_ribbon = 0

# Open the input file and process each line
with open(input_file_path, "r") as file:
    for line in file:
        # Parse dimensions from the line
        dimensions = list(map(int, line.strip().split("x")))
        
        # Calculate areas of the sides
        side1 = dimensions[0] * dimensions[1]
        side2 = dimensions[1] * dimensions[2]
        side3 = dimensions[2] * dimensions[0]
        
        # Calculate wrapping paper needed (surface area + smallest side)
        total_wrapping_paper += 2 * (side1 + side2 + side3) + min(side1, side2, side3)
        
        # Sort dimensions to calculate ribbon
        dimensions.sort()
        
        # Calculate ribbon needed (smallest perimeter + bow)
        total_ribbon += 2 * (dimensions[0] + dimensions[1]) + (dimensions[0] * dimensions[1] * dimensions[2])

# Print the results
print(total_wrapping_paper, total_ribbon)
