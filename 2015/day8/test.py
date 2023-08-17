import json
import re

def main():

    with open("day8/input.txt", "r") as file:
        string_count = 0
        decoded_string_count = 0
        encoded_string_count = 0
        for line in file:
            string_count += len(line)
            decoded_string_count += len(bytes(line, "utf-8").decode("unicode_escape")) - 2
            encoded_string_count += len(line.replace("\\", "\\\\").replace("\"", "\\\"")) + 2
        # part 1
        print(string_count - decoded_string_count)
        # part 2
        print(encoded_string_count - string_count)

if __name__ == "__main__":
    main()