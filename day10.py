def check_importance(cycle_num):
    if (cycle_num - 20) % 40 == 0 and cycle_num <= 220:
        return True
    return False


def solve_part_1(commands):
    cycle_counter = 0
    register_value = 1
    important_values = []

    for line in commands:
        if "addx" in line:
            for cycle in range(1, 3):
                if cycle == 1:
                    cycle_counter += 1
                    if check_importance(cycle_counter):
                        important_values.append(register_value * cycle_counter)
                else:
                    cycle_counter += 1
                    if check_importance(cycle_counter):
                        important_values.append(register_value * cycle_counter)
                    register_value += int(line.split(' ')[1])
        else:
            cycle_counter += 1
            if check_importance(cycle_counter):
                important_values.append(register_value * cycle_counter)

    print("Answer to part 1:", sum(value for value in important_values))


def print_pixel(cycle_num, reg_value):
    if cycle_num > 40:
        to_remove = int(cycle_num / 40)
        cycle_num = cycle_num - 40 * to_remove
    if (cycle_num-1) % 40 == 0:
        print()
    if abs(cycle_num - (reg_value + 1)) <= 1:
        print('#', end=" ")
    else:
        print('.', end=" ")


def solve_part_2(commands):
    cycle_counter = 0
    register_value = 1

    print("Answer to part 2:")
    for line in commands:
        if "addx" in line:
            for cycle in range(1, 3):
                if cycle == 1:
                    cycle_counter += 1
                    print_pixel(cycle_counter, register_value)
                else:
                    cycle_counter += 1
                    print_pixel(cycle_counter, register_value)
                    register_value += int(line.split(' ')[1])
        else:
            cycle_counter += 1
            print_pixel(cycle_counter, register_value)



if "__main__" == __name__:
    with open("day10_input.txt") as file:
        data = [i for i in file.read().strip().split('\n')]
    solve_part_1(data)
    solve_part_2(data)

