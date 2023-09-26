number_of_input = int(input())
total_sum = 0
for n in range(number_of_input):
    letter = input()
    total_sum += ord(letter)
print(f"The sum equals: {total_sum}")
