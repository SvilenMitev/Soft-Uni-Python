chat_list = []

while True:
    command = input().split()
    if command[0] == 'end':
        break
    elif command[0] == 'Chat':
        chat_list.append(command[1])
    elif command[0] == 'Delete':
        if command[1] in chat_list:
            chat_list.remove(command[1])
    elif command[0] == 'Edit':
        if command[1] in chat_list:
            index = chat_list.index(command[1])
            chat_list.remove(command[1])
            chat_list.insert(index, command[2])
    elif command[0] == 'Pin':
        if command[1] in chat_list:
            chat_list.remove(command[1])
            chat_list.append(command[1])
    elif command[0] == 'Spam':
        for i in (command):
            if i != 'Spam':
                chat_list.append(i)
print('\n'.join(chat_list))