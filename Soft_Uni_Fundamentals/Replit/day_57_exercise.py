def factorial_number(number:int)-> int:
    if number == 1:
        return 1
    else:
        return number * factorial_number(number-1)


print(factorial_number(10))
