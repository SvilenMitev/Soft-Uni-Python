number = int(input())

for i in range(1, number+1):
    digit_sum: int = 0
    current_number = str(i)
    for digit in current_number:
        digit_sum += int(digit)
    if digit_sum in {5, 7, 11}:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")