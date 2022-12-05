choiceMap =	{
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win"
} 
# Changed X,Y,Z from rock, paper, scissors, to lose, draw, win for Part 2
def resultChoice(choice, result):
    if(choiceMap[choice] == "rock" and result == "win"):
        return "B"
    if(choiceMap[choice] == "paper" and result == "win"):
        return "C"
    if(choiceMap[choice] == "scissors" and result == "win"):
        return "A"
    if(choiceMap[choice] == "rock" and result == "lose"):
        return "C"
    if(choiceMap[choice] == "paper" and result == "lose"):
        return "A"
    if(choiceMap[choice] == "scissors" and result == "lose"):
        return "B"
    return "ERROR"

opponentChoice = ''
myChoice = ''
winScore = 0 # The amount won for winning, losing, or drawing
choiceScore = 0 # The amount won for which choice you select; rock, paper, or scissors
totalScore = 0 # Total running score, never reset.

with open('strategyGuide.txt') as f:
    for line in f:
        opponentChoice = line[0]
        myChoice = line[2]
        if(choiceMap[myChoice] == "draw"):
            winScore = 3
            myChoice = opponentChoice
        elif(choiceMap[myChoice] == "win"):
            winScore = 6
            myChoice = resultChoice(opponentChoice, "win")
        elif(choiceMap[myChoice] == "lose"):
            winScore = 0
            myChoice = resultChoice(opponentChoice, "lose")

        # From Part 1
        # if(choiceMap[opponentChoice] == choiceMap[myChoice]):
        #     winScore = 3
        # elif((choiceMap[opponentChoice] == "rock" and choiceMap[myChoice] == "scissors") or
        #     (choiceMap[opponentChoice] == "scissors" and choiceMap[myChoice] == "paper") or
        #     (choiceMap[opponentChoice] == "paper" and choiceMap[myChoice] == "rock")):
        #     winScore = 0
        # elif((choiceMap[myChoice] == "rock" and choiceMap[opponentChoice] == "scissors") or
        #     (choiceMap[myChoice] == "scissors" and choiceMap[opponentChoice] == "paper") or
        #     (choiceMap[myChoice] == "paper" and choiceMap[opponentChoice] == "rock")):
        #     winScore = 6

        if(choiceMap[myChoice] == "rock"):
            choiceScore = 1
        elif(choiceMap[myChoice] == "paper"):
            choiceScore = 2
        elif(choiceMap[myChoice] == "scissors"):
            choiceScore = 3

        totalScore += choiceScore + winScore
        winScore = 0
        choiceScore = 0



    print(totalScore)

