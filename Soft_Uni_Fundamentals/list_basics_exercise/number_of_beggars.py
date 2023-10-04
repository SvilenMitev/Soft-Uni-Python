string_of_numbers = input()
my_list = string_of_numbers.split(", ")
number_of_beggars = int(input())
collected_money = []


for i in my_list:
    collected_money.append(int(i))
final_sum = []
start_index = 0
for n in range(number_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index,len(collected_money), number_of_beggars):
        current_beggar_sum += collected_money[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1
print(final_sum)