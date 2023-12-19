import math


total = []

for scratch in open("input.txt", "r").readlines():
    numbers = scratch.strip().split(" | ")
    list_of_numbers = numbers[1].replace("  ", " ").split(" ")
    winning_numbers = numbers[0].split(": ")[1].replace("  ", " ").split(" ")
    winnings = set(list_of_numbers) & set(winning_numbers)
    if winnings:
        if len(winnings) > 1:
            total.append(2 ** (len(winnings)-1))
        else:
            total.append(1)
    print(winnings, sum(total))