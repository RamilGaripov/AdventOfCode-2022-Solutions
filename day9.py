import numpy as np


def update_head_location(head, direction):
    if direction == "R":
        head["x"] += 1
    elif direction == "L":
        head["x"] -= 1
    elif direction == "U":
        head["y"] += 1
    elif direction == "D":
        head["y"] -= 1
    return head


def update_tail_location(head, tail):
    diff_x = head['x'] - tail['x']
    diff_y = head['y'] - tail['y']
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        tail['x'] += 1 * np.sign(diff_x)
        tail['y'] += 1 * np.sign(diff_y)
    return tail


def execute_step(step, knot_positions, tail_positions, num_of_knots):
    direction, num_of_steps = step.split(' ')
    num_of_steps = int(num_of_steps)
    for y in range(num_of_steps):
        knot_positions[0] = update_head_location(knot_positions[0], direction)
        for x in range(num_of_knots - 1):
            knot_positions[x+1] = update_tail_location(knot_positions[x], knot_positions[x+1])
            if x == num_of_knots-2:
                tail_positions.append((knot_positions[x+1]["x"], knot_positions[x+1]["y"]))
    return tail_positions


def initialize_solution(steps, tail_positions, num):
    knot_positions = []
    for x in range(num):
        knot_positions.append({"x": 0, "y": 0})
    print(knot_positions)
    for step in steps:
        tail_positions = execute_step(step, knot_positions, tail_positions, num)
    return tail_positions


if __name__ in "__main__":
    with open('day9_input.txt') as file:
        steps = [i for i in file.read().strip().split('\n')]
    tail_positions_part1 = []
    tail_positions_part2 = []

    tail_positions_part1 = initialize_solution(steps, tail_positions_part1, 2)
    tail_positions_part2 = initialize_solution(steps, tail_positions_part2, 10)

    print("Answer to part 1:", len(set(tail_positions_part1)))
    print("Answer to part 2:", len(set(tail_positions_part2)))

