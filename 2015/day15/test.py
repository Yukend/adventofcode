def maximum(s_, v):
    capacity = s_[0] * v[0]["capacity"] + s_[1] * v[1]["capacity"] + \
        s_[2] * v[2]["capacity"] + s_[3] * v[3]["capacity"]
    durability = s_[0] * v[0]["durability"] + s_[1] * v[1]["durability"] + \
        s_[2] * v[2]["durability"] + s_[3] * v[3]["durability"]
    flavor = s_[0] * v[0]["flavor"] + s_[1] * v[1]["flavor"] + \
        s_[2] * v[2]["flavor"] + s_[3] * v[3]["flavor"]
    texture = s_[0] * v[0]["texture"] + s_[1] * v[1]["texture"] + \
        s_[2] * v[2]["texture"] + s_[3] * v[3]["texture"]
    total = capacity * durability * flavor * texture
    return total


def combinations(v):
    maxi = 0
    for A in range(15, 83):
        for B in range(15, 83 - A):
            for C in range(15, 83 - A - B):
                D = 100 - A - B - C
                if D >= 1:
                    s_ = [A, B, C, D]
                    # part 1 run this after commend the part 2
                    total = maximum(s_, v)
                    if total > maxi:
                        maxi = total
                        print(maxi)
                    # part 2 run this after commend the part 1
                    if s_[0] * v[0]["calories"] + s_[1] * v[1]["calories"] + \
                            s_[2] * v[2]["calories"] + s_[3] * v[3]["calories"] == 500:
                        total = maximum(s_, v)
                        if total > maxi:
                            maxi = total
                            print(maxi)


if __name__ == "__main__":
    incrediants = {}
    for line in open("day15/input.txt", "r").readlines():
        l = line.replace(",", "").replace(":", "").split(" ")
        incrediants[l[0]] = {l[1]: int(l[2]), l[3]: int(
            l[4]), l[5]: int(l[6]), l[7]: int(l[8]), l[9]: int(l[10])}
    v = list(incrediants.values())
    combinations(v)
