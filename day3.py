# with open('day3_input.py') as file:
#
#     # Part1:
#     rucksacks = [i for i in file.read().strip().split("\n")]
#     totalPriorities = 0
#     print("ord(a)-96:", ord('a')-96)
#     print("ord(z)-96:", ord('z')-96)
#     print("ord(A)-38:", ord('A')-38)
#     print("ord(Z)-38:", ord('Z')-38)
#     num = 1
#     for sack in rucksacks:
#         numItemsInCompartment = int(len(sack)/2)
#         comp1 = sack[0:numItemsInCompartment]
#         comp2 = sack[numItemsInCompartment:]
#         letter = (set(comp1) & set(comp2)).pop()
#         if letter.isupper():
#             totalPriorities += ord(letter)-38
#         else:
#             totalPriorities += ord(letter)-96
#     answer1 = totalPriorities
#
    # # Part2:
    # elfNum = 0
    # totalPriorities = 0
    # for elf in rucksacks:
    #     elfNum += 1
    #     if elfNum == 1:
    #         elf1 = elf
    #     elif elfNum == 2:
    #         elf2 = elf
    #     else:
    #         elf3 = elf
    #         elfNum = 0
    #         badge = (set(elf1) & set(elf2) & set(elf3)).pop()
    #         if badge.isupper():
    #             # print("Letter", letter, "prior:", ord(letter)-38)
    #             totalPriorities += ord(badge) - 38
    #         else:
    #             # print("Letter", letter, "prior:", ord(letter) - 96)
    #             totalPriorities += ord(badge) - 96
    # answer2 = totalPriorities

#     # Answers:
#     print("Part1 answer:", answer1)
#     print("Part2 answer:", answer2)


import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase, 1):
    values[letter] = index
for index, letter in enumerate(string.ascii_uppercase, 27):
    values[letter] = index

# def rearrange(lines):
#     comp_1 = lines[:len(lines)//2]
#     comp_2 = lines[len(lines)//2:]
#     for letter in set(comp_1):
#         if letter in comp_2:
#
#             return values[letter]

def find_common(group):
    new_group = []
    for i in group:
        new_group.append(i.strip())
    for letter in set(new_group[0]):
        if letter in new_group[1]:
            if letter in new_group[2]:
                return values[letter]

if __name__ == '__main__':
    points = 0
    with open('day3_input.py') as f:
        lines = f.readlines()

    group_list = list(zip(*(iter(lines),)* 3))
    for group in group_list:
        points+=find_common(group)
    # for line in lines:
    #     points += rearrange(line)

    print(points)