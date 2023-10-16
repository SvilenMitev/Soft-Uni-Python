def add_subtract_number(list_of_numbers:list)->list:
    temp_list_of_numbers = []
    for i in list_of_numbers:
        if i <= popped_element:
            new_number = i + popped_element
            temp_list_of_numbers.append(new_number)
        else:
            new_number = i - popped_element
            temp_list_of_numbers.append(new_number)
    return temp_list_of_numbers


initial_string = input().split()
int_from_string = list(map(int, initial_string))
final_sum = 0
while len(int_from_string) != 0:
    current_number = int(input())
    if current_number < 0:
        current_number = 0
        popped_element = int_from_string.pop(0)
        final_sum += popped_element
        int_from_string.append(int_from_string[-1])
    elif current_number > len(int_from_string)-1:
        popped_element = int_from_string.pop(-1)
        final_sum += popped_element
        first_number = int_from_string[0]
        int_from_string.append(first_number)
    else:
        index = current_number
        popped_element = int_from_string.pop(index)
        final_sum += popped_element
    int_from_string = add_subtract_number(int_from_string)

print(final_sum)
