import re

equation = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMg" + \
    "YPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSi" + \
    "ThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArC" + \
    "aCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgA" + \
    "rPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBS" + \
    "iThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFA" + \
    "rCaSiAl"
# part 1.1
molecules = []
molecules_ = []

def nth_repl(sub, repl, n):
    find = equation.find(sub)
    i = find != -1
    while find != -1 and i != n:
        find = equation.find(sub, find + 1)
        i += 1
    if i == n:
        return equation[:find] + repl + equation[find+len(sub):]
    return equation


for line in open("day19/input.txt", "r").readlines():
    molecule = line.strip().replace(" ", "").split("=>")
    molecules_.append(tuple(molecule))
    count = equation.count(molecule[0])
    for i in range(1, count + 1):
        equation_ = nth_repl(molecule[0], molecule[1], i)
        molecules.append(equation_)
print(len(set(molecules)))

# part 1.2
with open('day19/input.txt') as f:
    lines = [x.strip().split() for x in f.readlines()]

replacements = [(x[0], x[2]) for x in lines[:-2]]

def make_combinations(s):
    for r in replacements: 
        for m in re.finditer(r[0], s):
            yield s[:m.start()] + r[1] + s[m.end():]


print(len(set(make_combinations(equation))))


# Part two
# Apparently, the greedy approach works just fine.
def make_removals(initial):
    for r in replacements:
        for m in re.finditer(r[1], initial):
            yield initial[:m.start()] + r[0] + initial[m.end():]


s = equation
i = 0
while s != 'e':
    shortest_len = float('inf')
    for removal in make_removals(s):
        if len(removal) < shortest_len:
            shortest_len = len(removal)
            shortest = removal
            print(i)
    s = shortest
    i += 1
print(i)