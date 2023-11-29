


initial_input = input()

while True:
    current_command = input()
    if current_command == 'Decode':
        break
    splited_command = current_command.split('|')
    command = splited_command[0] 
    if command == 'Move':
        numbers_to_move = int(splited_command[1])
        initial_input   = initial_input[numbers_to_move:] + initial_input [:numbers_to_move]
    elif command == 'Insert':
        index = int(splited_command[1])
        value = splited_command[2]
        initial_input = initial_input[:index] + value + initial_input[index:]
    elif command == 'ChangeAll':
        substring = splited_command[1]
        replacment = splited_command[2]
        # initial_input.replace(substring, replacment)
        result = ''
        for i in initial_input:
            if i == substring:
                result += replacment
            else:
                result += i
        initial_input = result

print(f"The decrypted message is: {initial_input}")
