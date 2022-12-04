# Sums up the elf calories and saves only the current and top 3 calories.
# Could turn this into a stored result that tracks the top list, but this uses less space.
with open('elfCalories.txt') as f:
    maxElfSum = 0
    maxElfSum2 = 0
    maxElfSum3 = 0
    elfSum = 0
    for line in f:
        if line == "\n":
            if elfSum >= maxElfSum:
                print(1)
                print(elfSum)
                maxElfSum3 = maxElfSum2
                maxElfSum2 = maxElfSum
                maxElfSum = elfSum
            elif elfSum >= maxElfSum2:
                print(2)
                print(elfSum)
                maxElfSum3 = maxElfSum2
                maxElfSum2 = elfSum
            elif elfSum >= maxElfSum3:
                print(3)
                print(elfSum)
                maxElfSum3 = elfSum
            elfSum = 0
            continue
        elfSum += int(line)

    print(maxElfSum + maxElfSum2 + maxElfSum3)
    print(maxElfSum)
    print(maxElfSum2)
    print(maxElfSum3)

