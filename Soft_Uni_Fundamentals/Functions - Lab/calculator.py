input_operator = input()
first_number = int(input())
second_number = int(input())


def calculator(operator, f_n, s_n):
    if operator == 'multiply':
        return f_n * s_n
    elif operator == 'divide':
        return int(f_n / s_n)
    elif operator == 'add':
        return f_n + s_n
    elif operator == 'subtract':
        return f_n - s_n


print(calculator(input_operator, first_number, second_number))
