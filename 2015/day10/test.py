rounds = 0

def calculate(inp):
    global rounds
    output = ""
    start = 0
    ne = 0
    for i in range(start, len(inp)):
        if i >= start:
            number = inp[start]
            if not start + 1 == len(inp) and number == inp[start + 1]:
                for j in range(ne, len(inp) - 1):
                    if inp[i] == inp[j+1]:
                        number = str(number) + str(inp[j+1])
                    else:
                        output = output + str(len(number)) + number[0]
                        break
                if i == len(inp) - 2:
                    output = output + str(len(number)) + number[0]
                    break
            else:
                output = output + str(len(number)) + number[0]
            start += len(number)
            ne += len(number)
    rounds += 1
    if rounds == 40:
        print(len(output)) 
    elif rounds == 50:
        return output
    else:
        print(len(output))
        return calculate(output)


if __name__ == "__main__":
    print(len(calculate("3113322113")))

sequence = "3113322113"

for _ in range(50):
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
    print(len(sequence))

result_length = len(sequence)
print(result_length)