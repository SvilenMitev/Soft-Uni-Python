input_list = input().split('!')

while True:
    command = input().split()
    if command[0] == "Go":
        break
    elif command[0] == "Urgent":
        if command[1] in input_list:
            continue
        else:
            input_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] not in input_list:
            continue
        else:
            input_list.remove(command[1])
    elif command[0] == "Correct":
        if command[1] not in input_list:
            continue
        # else:
        #     target_index = input_list.index(command[1])
        #     input_list[target_index] = command[2]

        else:
            old_item = command[1]
            new_item = command[2]
            if old_item in input_list:
                index = input_list.index(old_item)
                input_list[index] = new_item
    # elif command[0] == "Rearrange":
    #     if command[1] not in input_list:
    #         continue
    #     temp_item = input_list.remove(command[1])
    #     input_list.append(temp_item)

    # """cannot assign value based on remove method """

    elif command[0] == 'Rearrange':
        item = command[1]
        if item in input_list:
            input_list.remove(item)
            input_list.append(item)

print(', '.join(input_list))