key_number = int(input())
number_of_lines = int(input())
final_string = ''
for n in range(number_of_lines):
    new_letter = input()
    converted_letter = ord(new_letter)+key_number
    final_string += chr(converted_letter)

print(final_string)