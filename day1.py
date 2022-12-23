with open("day1_input.py") as file:
    data = [i for i in file.read().strip().split("\n")]
    sums = []
    totalPerElf = 0
    for calCount in data:
        if calCount != '':
            totalPerElf += int(calCount)
        else:
            sums.append(totalPerElf)
            totalPerElf = 0
    print('Answer to part 1:', max(sums))

    totalOfRichest = 0
    for index in range(0, 3):
        richest = max(sums)
        sums.remove(richest)
        totalOfRichest += richest
    print("Answer to part 2:", totalOfRichest)

