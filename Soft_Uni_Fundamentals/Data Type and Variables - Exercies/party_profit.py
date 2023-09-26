group_size = int(input())
number_of_days = int(input())

number_of_coins = 0

for n in range(1, number_of_days+1):
    number_of_coins += 50
    if n % 10 == 0:
        group_size -= 2
    if n % 15 == 0:
        group_size += 5
    number_of_coins -= 2*group_size

    if n % 3 == 0:
        number_of_coins -= 3 * group_size
    if n % 5 == 0:
        number_of_coins += 20 * group_size
        if n % 3 == 0:
            number_of_coins -= 2 * group_size

coins = number_of_coins // group_size
print(f"{group_size} companions received {coins} coins each.")

