total_dests = {}
for line in open("day14/input.txt", "r").readlines():
    inputs = line.split(" ")
    time = 0
    total_dest = 0
    while time < 2503:
        time = time + int(inputs[6]) + int(inputs[-2])
        total_dest = total_dest + (int(inputs[3]) * int(inputs[6]))
    total_dests[inputs[0]] = total_dest
print(max(total_dests.values()))