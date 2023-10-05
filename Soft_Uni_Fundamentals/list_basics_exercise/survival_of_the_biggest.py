numbers_input = input()
numbers_list = numbers_input.split()
numbers_to_remove = int(input())
converted_list = []
for i in numbers_list:
    converted_list.append(int(i))

for n in range(numbers_to_remove):
    converted_list.remove(min(converted_list))
output = ''
for j in converted_list:
    output += str(j)+", "
new_output = output[:-2]
print(new_output)
