import re


regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
current_input = input()

matches = re.finditer(regex, current_input)

for i in matches:
    print(i.group(), end=" ")

# import re

# number = input()
# pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
# matches = re.finditer(pattern, number)

# for match in matches:
#     print(match.group(), end=" ")