# part 1
def evaluate_signal(wire, signals, instructions):
    if wire in signals:
        return signals[wire]
    
    if wire.isdigit():
        return int(wire)

    instruction = instructions[wire]

    parts = instruction.split()
    if len(parts) == 1:
        print(parts)
        signals[wire] = evaluate_signal(parts[0], signals, instructions)
    elif len(parts) == 2:  # NOT operation
        signals[wire] = ~evaluate_signal(parts[1], signals, instructions) & 0xFFFF
    else:
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

def main():
    instructions = {}

    with open("day7/input.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" -> ")
            instructions[parts[1]] = parts[0]

    signals = {}
    signal_a = evaluate_signal("a", signals, instructions)
    print(f"The signal provided to wire a is: {signal_a}")

    # part 2
    # Override wire b with the signal obtained on wire a
    signals = {"b": signal_a}

    # Re-evaluate wire a with the new signals
    signal_a_override = evaluate_signal("a", signals, instructions)
    print(f"The new signal provided to wire a after overriding wire b is: {signal_a_override}")

if __name__ == "__main__":
    main()

