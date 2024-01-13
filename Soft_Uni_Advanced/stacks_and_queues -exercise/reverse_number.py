list_of_numbers = input().split(" ")
final_number = ""
for i in range(len(list_of_numbers)):
    final_number += f"{list_of_numbers.pop()} "
print(final_number)