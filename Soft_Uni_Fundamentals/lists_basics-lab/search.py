number_of_input = int(input())
special_word = input()
my_list = []
my_special_list = []
for n in range(number_of_input):
    new_word = input()
    my_list.append(new_word)
    if special_word in new_word:
        my_special_list.append(new_word)

print(my_list)
print(my_special_list)
