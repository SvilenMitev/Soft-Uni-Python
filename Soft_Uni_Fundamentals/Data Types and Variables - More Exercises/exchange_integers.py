first_number = int(input())
second_number = int(input())
temp_number = ''

print("Before:")
print(f"a = {first_number}")
print(f"b = {second_number}")

temp_number = first_number
first_number = second_number
second_number = temp_number



print("After:")
print(f"a = {first_number}")
print(f"b = {second_number}")