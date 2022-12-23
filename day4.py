

def createSet(elf_range):
    lower_bound, upper_bound = elf_range.split("-")
    new_set = {''}
    for x in range(int(lower_bound), int(upper_bound)+1):
        new_set.add(str(x))
    new_set.remove('')
    return new_set

if __name__ in "__main__":
    with open("day4_input.py") as file:
        data = [i for i in file.read().strip().split("\n")]
        answer1 = 0
        answer2 = 0
        for pair in data:
            elf1, elf2 = pair.split(',')
            elf1_set = createSet(elf1)
            elf2_set = createSet(elf2)
            if elf1_set.issubset(elf2_set) | elf2_set.issubset(elf1_set):
                answer1 += 1
            if elf1_set & elf2_set:
                answer2 += 1

        print("Answer to part1:", answer1)
        print("Answer to part2:", answer2)

