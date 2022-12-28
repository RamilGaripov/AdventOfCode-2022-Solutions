import re
from functools import reduce


class Monkey:
    def __init__(self, id=0, items=None, operation=None, test=None, action=[], activity=0) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.action = action
        self.activity = activity

    def print_properties(self):
        print("Monkey ID:", self.id,
              "\nItems:", self.items,
              "\nOperation:", self.operation,
              "\nTest:", self.test,
              "\nAction:", self.action,
              "\nTotal activity:", self.activity,
              "\n")


def get_monkeys_and_conditions(data):
    mon_list = []
    for id, monkey_data in enumerate(data):
        monkey = Monkey(id=id)
        targets = []
        for line in monkey_data.split("\n"):
            if "Starting items" in line:
                monkey.items = list(map(int, line.split(": ")[1].strip().split(",")))
            elif "Operation" in line:
                monkey.operation = line.split('old ')[1]
            elif "Test" in line:
                monkey.test = int(re.findall(r"\d+", line)[0])
            elif "If" in line:
                targets.append(int(re.findall(r"\d", line)[0]))

        monkey.action = targets
        mon_list.append(monkey)
    return mon_list


def inspect(init_worry, monkey, monkeys):
    crt = reduce(lambda acc, monk: acc*monk.test, monkeys, 1)
    second_num = monkey.operation.split(' ')[1]
    if 'old' in second_num:
        second_num = init_worry
    second_num = int(second_num)
    if "+" in monkey.operation:
        new_worry_level = init_worry + second_num
    else:
        new_worry_level = init_worry * second_num
    if num_is_large:
        return new_worry_level % crt
    return int(new_worry_level / 3)


def choose_target(item, test, targets):
    if item % test == 0:
        return targets[0]
    return targets[1]


def throw_item(src_monkey, target_monkey):
    src_monkey.activity += 1
    target_monkey.items.append(src_monkey.items.pop(0))


def monkey_business(all_monkeys):
    for monkey in all_monkeys:
        for index in range(len(monkey.items)):
            monkey.items[0] = inspect(monkey.items[0], monkey, all_monkeys)
            target = choose_target(monkey.items[0], monkey.test, monkey.action)
            throw_item(monkey, all_monkeys[target])


if "__main__" == __name__:
    with open("day11_input.txt") as file:
        monkeys_data = [i for i in file.read().strip().split("\n\n")]
    monkeys = get_monkeys_and_conditions(monkeys_data)
    for mon in monkeys:
        mon.print_properties()

    num_is_large = True
    if num_is_large:
        for game_round in range(10000):
            print(game_round)
            monkey_business(monkeys)
    else:
        for game_round in range(20):
            print(game_round)
            monkey_business(monkeys)

    for mon in monkeys:
        mon.print_properties()

    max1, max2 = 0, 0
    for monkey in monkeys:
        if max1 < monkey.activity:
            max2 = max1
            max1 = monkey.activity
        elif max2 < monkey.activity:
            max2 = monkey.activity
    print("Most active monkeys have activities of", max1, "and", max2)
    print("Their combined monkey business is", max1 * max2)
