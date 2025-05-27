# Define constants for vowels and forbidden substrings
VOWELS = {'a', 'e', 'i', 'o', 'u'}
FORBIDDEN_SUBSTRINGS = {'ab', 'cd', 'pq', 'xy'}

def is_nice_part1(word):
    """Check if a word is 'nice' according to part 1 rules."""
    # Count vowels
    vowel_count = sum(1 for char in word if char in VOWELS)
    # Check for forbidden substrings
    has_forbidden = any(sub in word for sub in FORBIDDEN_SUBSTRINGS)
    # Check for at least one double letter
    has_double = any(word[i] == word[i + 1] for i in range(len(word) - 1))
    # Return True if all conditions are met
    return vowel_count >= 3 and not has_forbidden and has_double

def is_nice_part2(word):
    """Check if a word is 'nice' according to part 2 rules."""
    # Check for a pair of letters appearing at least twice without overlapping
    has_pair = any(word[i:i + 2] in word[i + 2:] for i in range(len(word) - 1))
    # Check for a repeating letter with one letter in between
    has_repeating = any(word[i] == word[i + 2] for i in range(len(word) - 2))
    # Return True if both conditions are met
    return has_pair and has_repeating

def main():
    # Initialize counters for both parts
    total_part1 = 0
    total_part2 = 0

    # Open the input file and process each line
    with open("./day5/input.txt", "r") as file:
        for line in file:
            word = line.strip()
            # Check for part 1 and part 2 conditions
            if is_nice_part1(word):
                total_part1 += 1
            if is_nice_part2(word):
                total_part2 += 1

    # Print results
    print(f"Part 1: {total_part1}")
    print(f"Part 2: {total_part2}")

if __name__ == "__main__":
    main()
