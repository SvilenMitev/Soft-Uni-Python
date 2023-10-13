def to_do_list(my_list: list):
    output_list = sorted(my_list)
    final_list = []
    for split_item in (output_list):
        split = split_item.split('-')
        split.pop(0)
        final_list.extend(split)
    return final_list


my_do_list = []
while True:
    new_string = input()
    if new_string == 'End':
        break
    my_do_list.append(new_string)

print(to_do_list(my_do_list))
