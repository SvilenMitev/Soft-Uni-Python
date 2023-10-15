string_input = input().split('.')
for i in range(len(string_input)-1,-1,-1):
    index = int(i)
    current_number = int(string_input[index])
    if current_number == 9:
        string_input[index] = '0'
    else:
        string_input[index] = str(int(string_input[index]) + 1)
        break

print('.'.join(string_input))