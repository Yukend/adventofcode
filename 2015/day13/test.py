from itertools import permutations


with open("day13/input.txt", "r") as file:
    members = []
    happiness_bw_members = {}
    total_happiness = 0
    optimal_combination = []
    for line in file:
        line = line.rstrip().split(" ")
        members.append(line[0])
        happiness = int(line[3]) if line[2] == "gain" else -int(line[3])
        happiness_bw_members.__setitem__(line[0] + " to " + line[-1].replace(".", ""), happiness) 

    # part 1
    for combination in permutations(set(members)):
        combination = list(combination)
        pairs = []
        pairs.append(happiness_bw_members.get(combination[0] + " to " + combination[1]) + happiness_bw_members.get(combination[0] + " to " + combination[-1]))
        pairs.append(happiness_bw_members.get(combination[-1] + " to " + combination[-2]) + happiness_bw_members.get(combination[-1] + " to " + combination[0]))
        for i in range(1, len(combination)-1):
            value = happiness_bw_members.get(combination[i] + " to " + combination[i - 1]) + happiness_bw_members.get(combination[i] + " to " + combination[i + 1])
            pairs.append(value)
        mini = min(pairs)
        total = sum(pairs)
        if total > total_happiness:
            total_happiness = total
            optimal_combination = combination
            print(total_happiness)

    # part 2
    optimal_combination.insert(0, optimal_combination[-1])
    print(optimal_combination)
    for i in range(len(set(members))):
        total_happiness = total_happiness - (happiness_bw_members.get(optimal_combination[i + 1] + " to " + optimal_combination[i]) + happiness_bw_members.get(optimal_combination[i] + " to " + optimal_combination[i + 1]))
        print(total_happiness)
        total_happiness = total_happiness + (happiness_bw_members.get(optimal_combination[i + 1] + " to " + optimal_combination[i]) + happiness_bw_members.get(optimal_combination[i] + " to " + optimal_combination[i + 1])) 

