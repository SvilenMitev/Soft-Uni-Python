initial_string = input()
result_string = ''
for i in initial_string:
    if result_string == '':
        result_string += i
    if i == result_string[-1]:
        continue
    else:
        result_string += i

print(result_string)
