string_input = input().split()

result = [word for word in string_input if len(word) % 2 == 0]

for i in result:
    print(i)