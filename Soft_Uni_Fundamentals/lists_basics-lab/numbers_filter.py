number_of_input = int(input())
my_list = []
output_list = []
for i in range(number_of_input):
    current_number = int(input())
    my_list.append(current_number)

command = input()

if command == 'even':
    for n in my_list:
        if n % 2 == 0:
            output_list.append(n)
if command == 'odd':
    for n in my_list:
        if n % 2 != 0:
            output_list.append(n)
if command == 'negative':
    for n in my_list:
        if n < 0:
            output_list.append(n)
if command == 'positive':
    for n in my_list:
        if n >= 0:
            output_list.append(n)

print(output_list)
