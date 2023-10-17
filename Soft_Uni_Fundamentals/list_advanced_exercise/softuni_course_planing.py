list_of_subjects = input().split(', ')

while True:
    command = input().split(":")
    if command[0] == "course start":
        break
    elif command[0] == "Add":
        if command[1] not in list_of_subjects:
            list_of_subjects.append(command[1])
    elif command[0] == "Insert":
        if command[1] not in list_of_subjects:
            list_of_subjects.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if command[1] in list_of_subjects:
            list_of_subjects.remove(command[1])
            if (command[1] + "-Exercise") in list_of_subjects:
                list_of_subjects.remove((command[1] + "-Exercise"))
    elif command[0] == "Swap":
        if command[1] in list_of_subjects and command[2] in list_of_subjects:
            if (command[1]+"-Exercise") or (command[2]+"-Exercise") in list_of_subjects:
                a, b = list_of_subjects.index(command[1]), list_of_subjects.index(command[2])
                list_of_subjects[b], list_of_subjects[a] = list_of_subjects[a], list_of_subjects[b]
                if (command[1]+"-Exercise") in list_of_subjects:
                    list_of_subjects.remove((command[1]+"-Exercise"))
                    index = list_of_subjects.index(command[1]) +1
                    list_of_subjects.insert(index, (command[1]+"-Exercise"))
                elif (command[2] + "-Exercise") in list_of_subjects:
                    list_of_subjects.remove((command[2] + "-Exercise"))
                    index = list_of_subjects.index(command[2]) +1
                    list_of_subjects.insert(index, (command[2] + "-Exercise"))
            else:
                a, b = list_of_subjects.index(command[1]), list_of_subjects.index(command[2])
                list_of_subjects[b], list_of_subjects[a] = list_of_subjects[a], list_of_subjects[b]

    elif command[0] == "Exercise":
        if command[1] not in list_of_subjects:
            list_of_subjects.append(command[1])
            list_of_subjects.append(command[1]+"-Exercise")
        else:
            index = list_of_subjects.index(command[1]) + 1
            list_of_subjects.insert(index), (command[1] + "-Exercise")
    else:
        break

output = '\n'.join([str(x+1) + '.' + list_of_subjects[x] for x in range(len(list_of_subjects))])
print(output)
