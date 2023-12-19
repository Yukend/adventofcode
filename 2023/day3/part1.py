import re 


engine_schematic = [] 

total = 0

for part in open("input.txt", "r").readlines():
    engine_schematic.append("."+part.replace("\n", "")+".")
engine_schematic.insert(0, "."*len(engine_schematic[0]))
engine_schematic.insert(len(engine_schematic) + 1, "."*len(engine_schematic[0]))

for line in range(1, len(engine_schematic)):
    part_num = ""
    for index, num in enumerate(engine_schematic[line]):
        if index < len(engine_schematic[0]) and num.isdigit():
            part_num += str(num)
        else:
            for pos in range(1, len(part_num) + 1):
                adjucents = engine_schematic[line-1][index-len(part_num)+pos-2] + \
                            engine_schematic[line-1][index-len(part_num)+pos-1] + \
                            engine_schematic[line-1][index-len(part_num)+pos] + \
                            engine_schematic[line][index-len(part_num)+pos-2] + \
                            engine_schematic[line][index-len(part_num)+pos] + \
                            engine_schematic[line+1][index-len(part_num)+pos-2] + \
                            engine_schematic[line+1][index-len(part_num)+pos-1] + \
                            engine_schematic[line+1][index-len(part_num)+pos]
                if  re.search("[^\w\s\d.]", adjucents):
                        total += int(part_num)
                        break
            part_num = ""
print(total)