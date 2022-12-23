if __name__ in "__main__":
    with open('day8_input.txt') as file:
        data = [i for i in file.read().strip().split('\n')]
        for row in data:
            print(row, "\n")