first_string = input()

while True:
    command = input().split(":")
    if command == ["Travel"]:
        break
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index < len(first_string):
            # first_string[index] = string
            first_string = first_string[:index] + string + first_string[index:]
        print(first_string)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < len(first_string) and end_index < len(first_string):
            first_string= first_string[:start_index] + first_string[end_index+1:]
        print(first_string)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        while True:
            if old_string in first_string:
                first_string = first_string.replace(old_string, new_string)
            else:
                break
        print(first_string)


print(f"Ready for world tour! Planned stops: {first_string}")
