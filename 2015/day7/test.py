def evaluate_signal(wire, signals, instructions):
    """Recursively evaluates the signal for a given wire."""
    if wire in signals:  # Return cached signal if already computed
        return signals[wire]
    
    if wire.isdigit():  # Directly return numeric values
        return int(wire)

    instruction = instructions[wire]
    parts = instruction.split()

    if len(parts) == 1:  # Direct assignment
        signals[wire] = evaluate_signal(parts[0], signals, instructions)
    elif len(parts) == 2:  # NOT operation
        signals[wire] = ~evaluate_signal(parts[1], signals, instructions) & 0xFFFF
    else:  # Binary operations
        operand1 = evaluate_signal(parts[0], signals, instructions)
        operand2 = evaluate_signal(parts[2], signals, instructions)
        operator = parts[1]

        if operator == "AND":
            signals[wire] = operand1 & operand2
        elif operator == "OR":
            signals[wire] = operand1 | operand2
        elif operator == "LSHIFT":
            signals[wire] = operand1 << operand2
        elif operator == "RSHIFT":
            signals[wire] = operand1 >> operand2

    return signals[wire]

def parse_instructions(file_path):
    """Parses the input file and returns the instructions dictionary."""
    instructions = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(" -> ")
            instructions[parts[1]] = parts[0]
    return instructions

def main():
    input_file = "day7/input.txt"
    instructions = parse_instructions(input_file)

    # Part 1: Evaluate signal for wire 'a'
    signals = {}
    signal_a = evaluate_signal("a", signals, instructions)
    print(f"The signal provided to wire 'a' is: {signal_a}")

    # Part 2: Override wire 'b' with the signal from wire 'a' and re-evaluate
    signals = {"b": signal_a}
    signal_a_override = evaluate_signal("a", signals, instructions)
    print(f"The new signal provided to wire 'a' after overriding wire 'b' is: {signal_a_override}")

if __name__ == "__main__":
    main()
