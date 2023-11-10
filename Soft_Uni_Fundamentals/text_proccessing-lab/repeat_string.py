string_input = input().split()
result = ''
for word in string_input:
    lenghth = len(word)
    result += word*lenghth
print(result)