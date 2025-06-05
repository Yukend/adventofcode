def look_and_say(sequence, rounds):
    for _ in range(rounds):
        new_sequence = ""
        count = 1
        current_digit = sequence[0]

        for i in range(1, len(sequence)):
            if sequence[i] == current_digit:
                count += 1
            else:
                new_sequence += str(count) + current_digit
                count = 1
                current_digit = sequence[i]

        new_sequence += str(count) + current_digit
        sequence = new_sequence

    return sequence


if __name__ == "__main__":
    initial_sequence = "3113322113"
    result_40 = look_and_say(initial_sequence, 40)
    print(f"Length after 40 rounds: {len(result_40)}")

    result_50 = look_and_say(initial_sequence, 50)
    print(f"Length after 50 rounds: {len(result_50)}")
