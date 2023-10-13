number_list = list(map(int,input().split()))
happiness_multiplier = int(input())
new_list = []
for i in number_list:
    multiplied = i * happiness_multiplier
    new_list.append(multiplied)
avg_number = sum(new_list) / len(new_list)
#final_count = filter(lambda x: x in new_list if x > avg_number)
final_count = filter(lambda x: x if x > avg_number else False, new_list)
final_count_len = len(list(final_count))
if len(new_list) / 2 < final_count_len:
    print(f"Score: {final_count_len}/{len(new_list)}. Employees are happy!")
else:
    print(f"Score: {final_count_len}/{len(new_list)}. Employees are not happy!")