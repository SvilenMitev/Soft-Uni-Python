input_string = input().split()
final_result = ''
for i in input_string:
    ascii_value = ''
    word = ''
    for j in i:
        if j.isnumeric():
            ascii_value += j
        else:
            word += j
    ascii_value = chr(int(ascii_value))
    new_word = ascii_value+word
    new_list_as_word = []
    for i in new_word:
        new_list_as_word.append(i)
    new_list_as_word[1], new_list_as_word[-1] = new_list_as_word[-1], new_list_as_word[1]
    final_word = ''.join(new_list_as_word)
    final_result += ' '+final_word
print(final_result[1:])