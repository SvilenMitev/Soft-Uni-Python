first_string = input().split(', ')
second_string = input().split(', ')
final_list = []

for i in first_string:
    for j in second_string:
        if i in j:
            final_list.append(i)
            break
print(final_list)
