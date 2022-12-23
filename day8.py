def traverse_from_left(forest, visible_trees):
    for row_num in range(len(forest[0])):
        max_height = -1
        for col_num in range(len(forest)):
            if forest[row_num][col_num] > max_height:
                max_height = forest[row_num][col_num]
                visible_trees.append((row_num, col_num))
    return visible_trees


def traverse_from_right(forest, visible_trees):
    for row_num in range(len(forest[0])):
        max_height = -1
        for col_num in reversed(range(len(forest))):
            if forest[row_num][col_num] > max_height:
                max_height = forest[row_num][col_num]
                visible_trees.append((row_num, col_num))
    return visible_trees


def traverse_from_top(forest, visible_trees):
    for col_num in range(len(forest[0])):
        max_height = -1
        for row_num in range(len(forest)):
            if forest[row_num][col_num] > max_height:
                max_height = forest[row_num][col_num]
                visible_trees.append((row_num, col_num))
    return visible_trees


def traverse_from_bottom(forest, visible_trees):
    for col_num in range(len(forest[0])):
        max_height = -1
        for row_num in reversed(range(len(forest))):
            if forest[row_num][col_num] > max_height:
                max_height = forest[row_num][col_num]
                visible_trees.append((row_num, col_num))
    return visible_trees


def check_horizontally(row):
    target_tree = row[0]
    num_visible_trees = 0
    for tree in row[1:-1]:
        if target_tree > tree:
            num_visible_trees += 1
        else:
            num_visible_trees += 1
            break
    return num_visible_trees


def count_score(trees):
    count = 0
    for x in trees:
        count += 1
        if not x:
            break
    return count


def find_best_tree_house_spot(forest):
    scenic_scores = []
    for row_index, row in enumerate(forest[1:-1], 1):
        for col_index, tree in enumerate(row[1:-1], 1):
            row_left = [tree > x for x in row[:col_index]]
            row_right = [tree > x for x in row[col_index + 1:]]
            column_up = [tree > x[col_index] for x in forest[:row_index]]
            column_down = [tree > x[col_index] for x in forest[row_index + 1:]]

            score = count_score(row_left[::-1]) * count_score(row_right) * \
                    count_score(column_up[::-1]) * count_score(column_down)
            scenic_scores.append(score)
    return scenic_scores


if __name__ in "__main__":
    with open('day8_input.txt') as file:
        data = [i for i in file.read().strip().split('\n')]
    forest = []
    for index, row in enumerate(data):
        row_of_trees = []
        for tree in row:
            row_of_trees.append(int(tree))
        forest.append(row_of_trees)

    visible_trees = []
    visible_trees += traverse_from_left(forest, visible_trees)
    visible_trees += traverse_from_right(forest, visible_trees)
    visible_trees += traverse_from_top(forest, visible_trees)
    visible_trees += traverse_from_bottom(forest, visible_trees)
    visible_trees_set = set(visible_trees)
    print("Answer to part 1:", len(visible_trees_set))

    individual_tree_scores = find_best_tree_house_spot(forest)
    print("Answer to part 2:", max(individual_tree_scores))
