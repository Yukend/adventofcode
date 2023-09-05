letters = "abcdefghijklmnopqrstuvwxyz"


def inc_pw(pw):
    for i in range(len(pw)):
        if pw[i] == 25:
            pw[i] = 0
            continue
        else:
            pw[i]  += 1
            if 9 == pw[i] or 15 == pw[i] or 12 == pw[i]:
                pw[i] += 1
            break
    return pw


def solve(inp):
    data = [letters.index(inp) for inp in inp]

    pw = data
    while True:
        pw = inc_pw(pw)
        pairs = 0
        straight = 1
        l2 = pw[0]
        last = None
        found = False
        for i in pw:
            if i == l2 + 1:
                straight += 1
                if straight == 3:
                    found = True
            else:
                straight = 1
            if i == last:
                pairs += 1
                last = None
            else:
                last = i
            l2 = i
        if found and pairs >= 2:
            print("".join(letters[n] for n in pw)) 
        
    
solve("hepxcrrq")