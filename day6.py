def check_string(str):
    return len(set(str)) == len(str)


if __name__ in "__main__":
    with open('day6_input.txt') as file:
        data = file.read()
        start_of_packet = ''
        for x in range(len(data)):
            start_of_packet += data[x]
            if x >= 3:
                if len(start_of_packet) > 4:
                    start_of_packet = start_of_packet[1:]
                if check_string(start_of_packet):
                    print("Answer to part 1:", x+1)
                    break

        start_of_message = ''
        for x in range(len(data)):
            start_of_message += data[x]
            if x >= 14:
                if len(start_of_message) > 14:
                    start_of_message = start_of_message[1:]
                if check_string(start_of_message):
                    print("Answer to part 2:", x+1)
                    break
