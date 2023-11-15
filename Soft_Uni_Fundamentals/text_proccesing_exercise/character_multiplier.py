first_input = input().split(" ")

first_word = first_input[0]
second_word = first_input[1]
final_result = 0
diffrence = abs(len(first_word) - len(second_word))
if len(first_word) == len(second_word):
    for i in range(0, len(first_word), 1):
        final_result += ord(first_word[i]) * ord(second_word[i])
elif len(first_word) > len(second_word):
    for i in range(0, len(first_word) - diffrence, 1):
        final_result += ord(first_word[i]) * ord(second_word[i])
    for j in range(diffrence,0, -1):
        final_result += ord(first_word[j])
elif len(first_word) < len(second_word):
    for i in range(0, len(second_word) - diffrence, 1):
        final_result += ord(second_word[i]) * ord(first_word[i])

    for j in range(diffrence, 0, -1):
        final_result += ord(second_word[j])

print(final_result)