game_string = input()


while True:
    command = input().split(" ")
    if command[0] == "Done":
        break
    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        game_string = game_string.replace(char, replacement)
        print(game_string)
    elif command[0] == "Includes":
        string = command[1]
        if string in game_string:
            print(True)
        else:
            print(False)
    elif command[0] == "End":
        substring = command[1]
        end_string = len(substring)
        if substring == game_string[-end_string:]:
            print(True)
        else:
            print(False)
    elif command[0] == "Uppercase":
        game_string = game_string.upper()
        print(game_string)
    elif command[0] == "FindIndex":
        status = False
        char = command[1]
        find_index = -1
        for i in game_string:
            find_index += 1
            if i == char:
                status = True
                break

        if status:
            print(find_index)
    elif command[0] == "Cut":
        start_index = int(command[1])
        count = int(command[2])
        end_index = start_index + count
        cut_string = game_string[:start_index] + game_string[end_index:]
        game_string = game_string[start_index:end_index]
        print(game_string)
