import math


budget_input = float(input())
student_input = int(input())
price_for_flour = float(input())
price_for_single_egg = float(input())
price_for_single_apron = float(input())

eggs = student_input*price_for_single_egg*10
discount_flour = student_input // 5
flour = (student_input - discount_flour)* price_for_flour
apron = math.ceil(student_input * 1.2)*price_for_single_apron

total_price = eggs + flour + apron
needed_money = abs(budget_input - total_price)

if budget_input >= total_price:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f'{needed_money:.2f}$ more needed.')