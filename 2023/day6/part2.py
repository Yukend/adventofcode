input_data = {
    "time": 60808676,
    "distance": 601116315591300
}

ways_to_win = 0
for i, j in list(zip(range(1, input_data["time"]), reversed(range(input_data["time"])))):
    if i * j > input_data["distance"]:
        ways_to_win += 1

print(ways_to_win)
