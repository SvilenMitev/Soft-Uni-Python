def factorial_division(number:int) -> int:
    factorial_number = 1
    for i in range(1, number+1):
        factorial_number *= i
    return factorial_number


first_number = int(input())
second_number = int(input())
result = factorial_division(first_number)/factorial_division(second_number)
print(f"{result:.2f}")
