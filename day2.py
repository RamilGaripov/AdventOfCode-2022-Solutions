with open('day2_input.txt') as file:
    data = [i for i in file.read().strip().split('\n')]
    # ROCK: A, X
    # PAPER: B, Y
    # SCISSORS: C, Z

    # LOSE: X
    # DRAW: Y
    # WIN: Z

    # COMBINATIONS OF OUTCOMES:
    # A X: 4 | B X: 1 | C X: 7 |
    # A Y: 8 | B Y: 5 | C Y: 2 |
    # A Z: 3 | B Z: 9 | C Z: 6 |

    outcomes = {
        "A X": 1+3, "A Y": 2+6, "A Z": 3+0,
        "B X": 1+0, "B Y": 2+3, "B Z": 3+6,
        "C X": 1+6, "C Y": 2+0, "C Z": 3+3
    }

    totalPoints = 0
    for play in data:
        totalPoints += int(outcomes[play])
    answer1 = totalPoints

    totalPoints = 0
    desiredOutcomes = {
        "A X": 0+3, "A Y": 3+1, "A Z": 6+2,
        "B X": 0+1, "B Y": 3+2, "B Z": 6+3,
        "C X": 0+2, "C Y": 3+3, "C Z": 6+1
    }

    for play in data:
        totalPoints += int(desiredOutcomes[play])
    answer2 = totalPoints

    print("Answer to part 1:", answer1)
    print("Answer to part 2:", answer2)
