import sys
from itertools import permutations

# Read input and parse distances
places = set()
distances = {}

with open('day9/input.txt') as file:
    for line in file:
        source, _, dest, _, distance = line.split()
        places.update([source, dest])
        distances.setdefault(source, {})[dest] = int(distance)
        distances.setdefault(dest, {})[source] = int(distance)

# Calculate shortest and longest distances
shortest_distance = sys.maxsize
longest_distance = 0

for route in permutations(places):
    total_distance = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    shortest_distance = min(shortest_distance, total_distance)
    longest_distance = max(longest_distance, total_distance)

# Output results
print(f"Shortest distance: {shortest_distance}")
print(f"Longest distance: {longest_distance}")