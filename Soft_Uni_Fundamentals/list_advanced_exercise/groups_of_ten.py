string_input = input().split(', ')
list_with_int = list(map(int, string_input))

for i in range(0, max(list_with_int), 10):
    result_list = [number for number in list_with_int if i < number <= i + 10]
    print(f"Group of {i+10}'s: {result_list}")
