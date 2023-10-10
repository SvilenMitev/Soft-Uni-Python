

string_input = input().split()
int_input = []
for i in string_input:
    int_input.append(int(i))

print(sorted(int_input))