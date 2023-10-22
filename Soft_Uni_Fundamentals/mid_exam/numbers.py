initial_input = input().split()

while True:
    command = input().split()
    if command[0] == "Finish":
        break
    elif command[0] == "Add":
        initial_input.append(command[1])
    elif command[0] == "Remove":
        initial_input.remove(command[1])
    elif command[0] == "Replace":
        index = initial_input.index(command[1])
        initial_input.remove(command[1])
        initial_input.insert(index, command[2])
    elif command[0] == "Collapse":
        temp_list = []
        for i in initial_input:
            if int(i) >= int(command[1]):
                temp_list.append(i)
        initial_input = temp_list
print(' '.join(initial_input))
