thisDict = {
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16,
    "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26
}

# Part 1
with open('input.txt') as f:
    totalSum = 0
    for line in f:
        mid = len(line) // 2
        left = slice(0,mid)
        right = slice(mid, len(line))
        for char in line[left]:
            if char in line[right]:
                if char != char.lower():
                    totalSum += thisDict[char.lower()] + 26
                else:
                    totalSum += thisDict[char]
                break
    print(totalSum)
with open('input.txt') as f:
    result = 0
    for index, line in enumerate(f):
            line1 = line
            line2 = next(f)
            line3 = next(f)
            for char in line1:
                if char in line2:
                    if char in line3:
                        if char != char.lower():
                            result += thisDict[char.lower()] + 26
                        else:
                            result += thisDict[char]
                        break
    print(result)
