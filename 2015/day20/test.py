def find_lowest_house_number(target_presents):
    # Create an array to track the number of presents at each house
    houses = [0] * (target_presents // 10)

    for elf in range(1, len(houses) + 1):
        for house in range(elf - 1, len(houses), elf):
            houses[house] += elf * 10

    for house, presents in enumerate(houses):
        if presents >= target_presents:
            return house + 1  # House numbering starts from 1

    return None

target_presents = 33100000
lowest_house_number = find_lowest_house_number(target_presents)
print("Lowest house number:", lowest_house_number)

import numpy as np


n = 33100000

# Part one
presents = np.zeros(n//10)
for elf in range(1, n//10):
    for house in range(elf, n//10, elf):
        presents[house] += elf * 10
print(np.argmax(presents >= n))

# Part two
presents = np.zeros(n//10)
for elf in range(1, n//10):
    for house in range(elf, n//10, elf):
        presents[house] += elf * 11
        if house == 50*elf:
            break
print(np.argmax(presents >= n))