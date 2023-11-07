initial_input = input()
count_dict = {}

for i in (initial_input):
    if i == " ":
        continue
    elif i not in count_dict:
        count_dict[i] = 0
    count_dict[i] += 1

for keys, values in count_dict.items():
    print(f"{keys} -> {values}")
    