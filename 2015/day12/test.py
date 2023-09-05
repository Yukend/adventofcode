import re
import json

for line in open("day12/input.txt", "r").readlines():
    matches = re.findall("[-]?\d+", line)
    # part 1
    print(sum([int(i) for i in matches]))

    # part 2
    def sum_without_red(obj):
        if isinstance(obj, int):
            return obj

        if isinstance(obj, list):
            return sum(sum_without_red(item) for item in obj)

        if isinstance(obj, dict):
            if "red" in obj.values():
                return 0

            return sum(sum_without_red(value) for value in obj.values())

        return 0

    print(sum_without_red(json.loads(line)))
