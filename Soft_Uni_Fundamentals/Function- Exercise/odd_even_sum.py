def odd_or_even(number):
    even_number = 0
    odd_number = 0
    for i in (number):
        if int(i) % 2 == 0:
            even_number += int(i)
        else:
            odd_number += int(i)
    return odd_number, even_number


input_number = input()
sum_of_odd_digests, sum_of_even_digits = odd_or_even(input_number)
print(f"Odd sum = {sum_of_odd_digests}, Even sum = {sum_of_even_digits}")
