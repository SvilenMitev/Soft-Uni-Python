initial_input = input()

is_number = ''
is_alpha = ''
is_other = ''

for i in initial_input:
    if i.isalpha():
        is_alpha += i
    elif i.isnumeric():
        is_number += i
    else:
        is_other += i

print(f"{is_number}\n{is_alpha}\n{is_other}")