from itertools import combinations


containers = [1, 6, 13, 13, 14, 16, 18, 18, 20, 24, 30, 33, 35, 35, 41, 42, 44, 45, 48, 50]
# part 1
count = 0
for i in range(3, 11):
    for comb in combinations(containers, i):
        if sum(comb) == 150:
            count += 1
print(count)

# part 2
count = 0
for comb in combinations(containers, 4):
    if sum(comb) == 150:
        count += 1
print(count)