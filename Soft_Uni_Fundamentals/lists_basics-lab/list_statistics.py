number_of_inputs = int(input())
count_of_positive_list = []
sum_of_negative_list = []

for i in range(number_of_inputs):
    current_number = int(input())
    if current_number >= 0:
        count_of_positive_list.append(current_number)
    elif current_number < 0:
        sum_of_negative_list.append(current_number)

print(count_of_positive_list)
print(sum_of_negative_list)
print(f"Count of positives: {len(count_of_positive_list)}")
print(f"Sum of negatives: {sum(sum_of_negative_list)}")
