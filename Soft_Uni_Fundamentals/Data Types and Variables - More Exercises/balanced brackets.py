number_of_input = int(input())
count = 0
balanced = True
for i in range(number_of_input):
    new_input = input()
    if new_input == "(":
        count += 1
    elif new_input == ")":
        count -= 1
    if count < 0 or count >1:
        balanced = False
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")


