import re 


engine_schematic = [] 

total = 0

for part in open("input.txt", "r").readlines():
    engine_schematic.append("..."+part.replace("\n", "")+"...")
for i in range(0, 3):
    engine_schematic.insert(0, "."*len(engine_schematic[0]))
    engine_schematic.insert(len(engine_schematic) + 1, "."*len(engine_schematic[0]))
print(engine_schematic)
for row in range(3, len(engine_schematic)-3):
    gear_ratio = []
    for _index, _char in enumerate(engine_schematic[row][3:13]):
        if re.match("[*]", _char):
            u_row = engine_schematic[row-1][_index-5:_index+5]
            s_row = engine_schematic[row][_index-5:_index+5]
            b_row = engine_schematic[row+1][_index-5:_index+5]
            print(u_row, s_row, b_row)
            gears = {"u_row": re.findall("\d{2,3}", u_row), "s_row": re.findall("\d{2,3}", s_row), "b_row":re.findall("\d{2,3}", b_row)}
            for number in gears["u_row"]:
                sub_str = s_row[u_row.index(number)-1:u_row.index(number)+len(number)+1]
                if re.match("[*]", sub_str): 
                    gear_ratio.append(number)
            for number in gears["s_row"]:
                if s_row.index(number) == _index-len(number) or s_row.index(number) == _index + 1: 
                    gear_ratio.append(number)
            for number in gears["b_row"]:
                sub_str = s_row[b_row.index(number)-1:b_row.index(number)+len(number)+1]
                if re.match("[*]", sub_str): 
                    gear_ratio.append(number)
    print(gear_ratio)
    if len(gear_ratio) == 2:
        total += int(gear_ratio[0]) * int(gear_ratio[1])
print(total)
        


    
    