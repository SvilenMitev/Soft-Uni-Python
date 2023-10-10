def characters_in_range(first, second):
    my_string = ''
    for i in range(ord(first)+1, ord(second)):
        my_string += chr(i) + ' '
    return my_string

first_input = input()
second_input = input()
print(characters_in_range(first_input, second_input))
