current_input = input().split()
dict_task = {}

for i in current_input:
    i_lower = i.lower()
    if i_lower not in dict_task:
        dict_task[i_lower] = 0
    dict_task[i_lower] += 1

for key, value in dict_task.items():
    if value % 2 != 0:
        print(key, end=" ")


# if i_lower in dict_task:
#     dict_task.pop(i_lower)
# elif i_lower not in dict_task:
#     dict_task[i_lower] = i_lower