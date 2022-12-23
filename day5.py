import re
import copy

stacks = {
    1: ["F", "C", "P", "G", "Q", "R"],
    2: ["W", "T", "C", "P"],
    3: ["B", "H", "P", "M", "C"],
    4: ["L", "T", "Q", "S", "M", "P", "R"],
    5: ["P", "H", "J", "Z", "V", "G", "N"],
    6: ["D", "P", "J"],
    7: ["L", "G", "P", "Z", "F", "J", "T", "R"],
    8: ["N", "L", "H", "C", "F", "P", "T", "J"],
    9: ["G", "V", "Z", "Q", "H", "T", "C", "W"]
}

stacksPart1 = copy.deepcopy(stacks)
stacksPart2 = copy.deepcopy(stacks)


def execute_operation9000(stacks_p1, num, from_crate, to_crate):
    for x in range(num):
        popped_crates = stacks_p1[from_crate].pop()
        stacks_p1[to_crate].append(popped_crates)
    return stacks_p1


def execute_operation9001(stacks_p2, num, from_crate, to_crate):
    num_crates_from_stack = len(stacks_p2[from_crate])
    from_num = num_crates_from_stack - num
    taken = stacks_p2[from_crate][from_num::]
    stacks_p2[from_crate] = stacks_p2[from_crate][0:from_num]
    stacks_p2[to_crate] = stacks_p2[to_crate] + taken
    return stacks_p2


if __name__ in "__main__":
    with open("day5_input.txt") as file:
        data = [i for i in file.read().strip().split("\n")]

    for operation in data:
        move = re.findall(r"\d+", operation)
        if move:
            numCratesToMove = int(move[0])
            fromCrate = int(move[1])
            toCrate = int(move[2])
            stacksPart1 = execute_operation9000(stacksPart1, numCratesToMove, fromCrate, toCrate)
            stacksPart2 = execute_operation9001(stacksPart2, numCratesToMove, fromCrate, toCrate)

    print("Answer to part 1:", end=" ")
    for x in range(1, 10):
        print(stacksPart1[x][len(stacksPart1[x]) - 1], end="")

    print("\nAnswer to part 2:", end=" ")
    for y in range(1, 10):
        print(stacksPart2[y][len(stacksPart2[y]) - 1], end="")

