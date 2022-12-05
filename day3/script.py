thisDict = {
    "a" : 1, "b" : 2, "c" : 3
}

with open('input.txt') as f:
    for line in f:
        mid = len(line) // 2
        left = slice(0,mid)
        right = slice(mid, len(line))

        for char in line[left]:
            if char in line[right]:
                print(char)
