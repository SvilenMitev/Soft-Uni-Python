raw_activation_key = input()


while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        break
    if command[0] == "Contains":
        string = command[1] 
        if string in raw_activation_key:
            print(f"{raw_activation_key} contains {string}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == 'Upper':
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
        elif command[1] == 'Lower':
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif command[0]== "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)


print(f"Your activation key is: {raw_activation_key}")