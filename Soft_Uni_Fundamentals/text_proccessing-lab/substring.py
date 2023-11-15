first_input = input()
second_input = input()

while True:
    if first_input in second_input:
        second_input = second_input.replace(first_input, '')
    else:
        break

print(second_input)