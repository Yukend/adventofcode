import re 

seeds = []
connection = {}
connection_key= ""
for line in open("input.txt", "r").readlines():
    if line.startswith("seeds:"):
        seeds = line.strip().replace("seeds: ","").split(" ")
    elif re.match("^[a-z- ]", line.strip()):
        connection_key = line.strip().replace(":", "")
        connection[connection_key] = {}
    elif re.match("^[0-9]", line.strip()):
        ranges = line.strip().split(" ")
        connection[connection_key][ranges[1]+"-"+ranges[2]] = ranges[0]
soils = {}
for seed in seeds:
    soils[seed] = int(seed)
    for src, dest in connection.get("seed-to-soil map").items():
        src_range = src.split("-")
        if int(src_range[0]) <= int(seed) < int(src_range[0]) + int(src_range[1]):
            soils[seed] = (int(dest) + (int(seed) - int(src_range[0])))
fertilizers = {}
print(set(soils.values()))
for soil in soils.values():
    fertilizers[soil] = int(soil)
    for src, dest in connection.get("soil-to-fertilizer map").items():
        src_range = src.split("-")
        if int(src_range[0]) <= int(soil) < int(src_range[0]) + int(src_range[1]):
            fertilizers[soil] = (int(dest) + (int(soil) - int(src_range[0])))
waters = {}
print(set(fertilizers.values()))
for fertilizer in fertilizers.values():
    waters[fertilizer] = int(fertilizer)
    for src, dest in connection.get("fertilizer-to-water map").items():
        src_range = src.split("-")
        if int(src_range[0]) <= int(fertilizer) < int(src_range[0]) + int(src_range[1]):
            waters[fertilizer] = (int(dest) + (int(fertilizer) - int(src_range[0])))
lights = {}
print(set(waters.values()))
for water in waters.values():
    lights[water] = int(water)
    for src, dest in connection.get("water-to-light map").items():
        src_range = src.split("-")
        if int(src_range[0]) <= int(water) < int(src_range[0]) + int(src_range[1]):
            lights[water] = (int(dest) + (int(water) - int(src_range[0])))
temperatures = {}
print(set(lights.values()))
for light in lights.values():
    temperatures[light] = int(light)
    for src, dest in connection.get("light-to-temperature map").items():
        src_range = src.split("-")
        if int(src_range[0]) <= int(light) < int(src_range[0]) + int(src_range[1]):
            temperatures[light] = (int(dest) + (int(light) - int(src_range[0])))
humiditys = {}
print(set(temperatures.values()))
for temperature in temperatures.values():
    humiditys[temperature] = int(temperature)
    for src, dest in connection.get("temperature-to-humidity map").items():
        src_range = src.split("-")
        if int(src_range[0]) <= int(temperature) < int(src_range[0]) + int(src_range[1]):
            humiditys[temperature] = (int(dest) + (int(temperature) - int(src_range[0])))
locations = {}
print(set(humiditys.values()))
for humidity in humiditys.values():
    locations[humidity] = int(humidity)
    for src, dest in connection.get("humidity-to-location map").items():
        src_range = src.split("-")
        if int(src_range[0]) <= int(humidity) < int(src_range[0]) + int(src_range[1]):
            locations[humidity] = (int(dest) + (int(humidity) - int(src_range[0])))
print(min(set(locations.values())))