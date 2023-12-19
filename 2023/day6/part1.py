input_data = [{
    "time": 60,
    "distance": 601
},
    {
    "time": 80,
    "distance": 1163
},
    {
    "time": 86,
    "distance": 1559
},
    {
    "time": 76,
    "distance": 1300
}]

record_total = 1
for round in input_data:
    ways_to_win = 0
    for i, j in list(zip(range(1, round["time"]), reversed(range(round["time"])))):
        if i * j > round["distance"]:
            ways_to_win += 1
    record_total *= ways_to_win

print(record_total)
