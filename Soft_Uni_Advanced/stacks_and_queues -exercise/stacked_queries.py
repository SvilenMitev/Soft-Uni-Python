number_of_input = int(input())
stack_of_numbers = []
result = []
for i in range (number_of_input):
    command = input()
    if command[0] == '1':
        split = command.split(" ")
        stack_of_numbers.append(int(split[1]))
    elif command[0] == "2" and len(stack_of_numbers) > 0:
        stack_of_numbers.pop()
    elif command[0] == "3" and len(stack_of_numbers) > 0 :
        print(max(stack_of_numbers))
    elif command[0] == "4" and len(stack_of_numbers) > 0:
        print(min(stack_of_numbers))

for i in range(len(stack_of_numbers)):
    test = stack_of_numbers.pop()
    result.append(str(test))

print(", ".join(result))   

