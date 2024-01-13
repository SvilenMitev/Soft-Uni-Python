current_string = list(input())
reversed_list = []
for i in range(len(current_string)):
    popped_item = current_string.pop()
    reversed_list.append(popped_item)
print("".join(reversed_list))
