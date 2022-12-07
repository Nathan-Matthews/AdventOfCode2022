# Part 1
with open("input.txt") as f:
    result = 0
    for line in f:
        elf1, elf2 = line.split(",")
        e1a1,e1a2 = elf1.split("-")
        e2a1,e2a2 = elf2.split("-")
        e1a1 = int(e1a1)
        e1a2 = int(e1a2)
        e2a1 = int(e2a1)
        e2a2 = int(e2a2)
        if(e1a1 <= e2a1 and e1a2 >= e2a2):
            result += 1
            print(e1a1,e1a2,e2a1,e2a2)
        elif(e1a1 >= e2a1 and e1a2 <= e2a2):
            result += 1
            print(e1a1,e1a2,e2a1,e2a2)
    print(result)
# Part 2
with open("input.txt") as f:
    result2 = 0
    for line in f:
        elf1, elf2 = line.split(",")
        e1a1,e1a2 = elf1.split("-")
        e2a1,e2a2 = elf2.split("-")
        e1a1 = int(e1a1)
        e1a2 = int(e1a2)
        e2a1 = int(e2a1)
        e2a2 = int(e2a2)
        count1 = e1a1
        while(count1 <= e1a2):
            if count1 == e2a1 or count1 == e2a2:
                result2 += 1
                print(e1a1,e1a2,e2a1,e2a2)
                break
            if(e1a1 >= e2a1 and e1a2 <= e2a2):
                result2 += 1
                print(e1a1,e1a2,e2a1,e2a2)
                break
            count1 += 1

    print(result2)