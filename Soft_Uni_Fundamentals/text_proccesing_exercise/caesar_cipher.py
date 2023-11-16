initial_input = input()
final_result = ''
for i in initial_input:
    j = ord(i) + 3
    final_result += chr(j)

print(final_result)
