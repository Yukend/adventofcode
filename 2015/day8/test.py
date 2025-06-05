def main():
    try:
        # Open the input file
        with open("day8/input.txt", "r") as file:
            string_count = 0
            decoded_string_count = 0
            encoded_string_count = 0

            # Process each line in the file
            for line in file:
                line = line.strip()  # Remove any trailing newline or whitespace
                string_count += len(line)
                decoded_string_count += len(bytes(line, "utf-8").decode("unicode_escape")) - 2
                encoded_string_count += len(line.replace("\\", "\\\\").replace("\"", "\\\"")) + 2

            # Part 1: Difference between string count and decoded string count
            print("Part 1:", string_count - decoded_string_count)

            # Part 2: Difference between encoded string count and string count
            print("Part 2:", encoded_string_count - string_count)

    except FileNotFoundError:
        print("Error: The file 'day8/input.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()