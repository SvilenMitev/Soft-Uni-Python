initial_input = input().split()
bakary_dict = {}
for i in range(0, len(initial_input), 2):
    key = initial_input[i]
    value = initial_input[i+1]
    bakary_dict[key] = int(value)
print(bakary_dict)