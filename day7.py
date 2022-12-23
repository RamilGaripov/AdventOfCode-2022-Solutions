import re
from collections import defaultdict

if __name__ in "__main__":
    with open('day7_input.txt') as file:
        data = [i for i in file.read().strip().split('\n')]

    current_dir_tree = []
    path_with_size = {}
    dirs_with_sizes = defaultdict(int)
    for line in data:
        if "$ cd" in line:
            if "/" in line:
                current_dir_tree.append("root")
            elif ".." in line:
                current_dir_tree.pop()
            else:
                current_dir_tree.append(current_dir_tree[-1] + "/" + re.findall(r"(?<=cd ).+", line)[0])
        elif line[0].isdigit():
            size = int(line.split(" ")[0])
            for path in current_dir_tree:
                dirs_with_sizes[path] += size

    print("Answer to part 1:", sum(size for size in dirs_with_sizes.values() if size <= 100000))

    print("Answer to part 2:", min(size for size in dirs_with_sizes.values() if size >= dirs_with_sizes['root'] - 40000000))
