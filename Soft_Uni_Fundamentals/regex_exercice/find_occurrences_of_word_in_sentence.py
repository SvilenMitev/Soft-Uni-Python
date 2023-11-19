import re


first_input = input()
word = input()

regex = fr'(?i)\b{word}\b'

matches = re.findall(regex, first_input)

print(len(matches))