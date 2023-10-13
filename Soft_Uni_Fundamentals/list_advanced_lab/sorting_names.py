def sort_string(list_input:list):
    new_string = sorted(list_input, key=lambda x: (-len(x), x))
    return new_string


input_string = input().split(', ')
print(sort_string(input_string))