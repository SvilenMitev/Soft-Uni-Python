from collections import deque

def is_negative_number(s):
    try:
        num = float(s)
        return True
    except ValueError:
        return False
first_string = input().split()
my_dec = deque(first_string)
temp_list = deque()
final_number = int(my_dec.popleft())  # Initialize final_number as an integer

while my_dec:
    item = my_dec.popleft()
    if is_negative_number(item):
        temp_list.append(item)
    else:
        for y in temp_list:
            if item == '-':
                final_number -= int(y)
            elif item == '+':
                final_number += int(y)
            elif item == '*':
                final_number *= int(y)
            elif item == '/':
                final_number //= int(y)
        temp_list = deque() # Reset temp_list as a deque

print(int(final_number))
