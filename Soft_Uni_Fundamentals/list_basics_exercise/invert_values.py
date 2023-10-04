initial_string = input()
my_list = initial_string.split()
reverted_list = []
for n in my_list:
    if int(n) >= 0:
        reverted_number = -abs(int(n))
    else:
        reverted_number = abs(int(n))
    reverted_list.append(reverted_number)

print(reverted_list)
