

string_input = input().split()
int_list = []
for i in string_input:
    int_list.append(int(i))

new_string = filter(lambda n: n % 2 == 0, int_list)
print(list(new_string))
