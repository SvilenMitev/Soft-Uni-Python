def min_max_sum (input_int:list):
    min_number = min(input_int)
    max_number = max(input_int)
    sum_number = sum(input_int)
    return f"The minimum number is {min_number} \n" f"The maximum number is {max_number} \n" f"The sum number is: {sum_number}"
string_input = input().split()
int_input = []
for i in string_input:
    int_input.append(int(i))
print(min_max_sum(int_input))


