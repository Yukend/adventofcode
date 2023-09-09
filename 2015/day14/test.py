total_dests = {}
description_dict = {}
distance = {}
travel = {}
rest = {}
out = {}
for line in open("day14/input.txt", "r").readlines():
    inputs = line.split(" ")
    description_dict[inputs[0]] = {"distance": int(inputs[3]), "travel_time": int(inputs[6]), "rest": False, "rest_time": int(inputs[-2]) }
    distance[inputs[0]] = 0
    out[inputs[0]] = 0
    travel[inputs[0]] = int(inputs[6]) 
    rest[inputs[0]] = int(inputs[-2]) 
    time = 0
    total_dest = 0
    # part 1
    while time < 2503:
        time = time + int(inputs[6]) + int(inputs[-2])
        total_dest = total_dest + (int(inputs[3]) * int(inputs[6]))
    total_dests[inputs[0]] = total_dest
    print(max(total_dests.values()))

# Part 2: Simulate the race and calculate points
for i in range(0, 2503):
    for key, value in description_dict.items():
        if value["rest"]:
            if rest[key] == 0:
                travel[key] = value["travel_time"] - 1
                value["rest"] = False
            else:
                rest[key] -= 1
        else:
            if travel[key] == 0:
                rest[key] = value["rest_time"] - 1
                value["rest"] = True
            else:
                distance[key] += value["distance"]
                travel[key] -= 1

    maxi = max(distance.values())
    for k, v in distance.items():
        if v == maxi:
            out[k] += 1

print("Part 2: Winner's points:", out)

# from collections import defaultdict


# with open('day14/input.txt') as f:
#     lines = [x.strip().split() for x in f.readlines()]


# def get_distance(v, tt, tr, maxt):
#     t = 0
#     d = 0
#     while True:
#         for _ in range(tt):
#             d += v
#             t += 1
#             if t == maxt:
#                 return d
#         t += tr
#         if t >= maxt:
#             return d


# # Part one
# best = -float('inf')
# for l in lines:
#     distance = get_distance(int(l[3]), int(l[6]), int(l[-2]), 2503)
#     best = max(best, distance)
# print(best)

# # Part two
# points = defaultdict(int)
# for t in range(1, 2504):
#     best = -float('inf')
#     winners = []
#     for l in lines:
#         distance = get_distance(int(l[3]), int(l[6]), int(l[-2]), t)
#         if distance >= best:
#             if distance == best:
#                 winners.append(l[0])
#             else:
#                 winners = [l[0]]
#             best = max(best, distance)
#     for winner in winners:
#         points[winner] += 1
# print(max(points.values()))
        

    
