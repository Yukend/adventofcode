with open("./day5/input.txt", "r") as file:
    # part 1 
    total = 0
    total_2 = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    substring = ['ab','cd','pq','xy']
    for line in file.readlines():
        word = line.strip()
        vowel_count =  sum([1 for i in word if i in vowel])
        substring_in = sum([1 for j in range(len(word) - 1) if word[j] + word[j+1] in substring])
        doublestring_in = sum([1 for j in range(len(word) - 1) if word[j] == word[j+1]])
        if vowel_count >= 3 and substring_in == 0 and doublestring_in >= 1:
            total += 1

        # part 2
        pairs = [word[j] + word[j+1] for j in range(len(word)-1) if word[j] + word[j+1] in word[j+2:]]
        sequence = [word[j] + word[j+1] + word[j+2] for j in range(len(word)-2) if word[j] == word[j+2]]
        if pairs and sequence:
            total_2 += 1
    print(total)
    print(total_2)


