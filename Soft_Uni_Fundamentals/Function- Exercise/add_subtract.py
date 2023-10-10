def sum_numbers(first, second):
    return first + second


def subtract(sum_first, third):
    return sum_first - third


def add_and_subtract(first, second, third):
    sum_of_fist_two_numbers = sum_numbers(first, second)
    result = subtract(sum_of_fist_two_numbers, third)
    return result

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
