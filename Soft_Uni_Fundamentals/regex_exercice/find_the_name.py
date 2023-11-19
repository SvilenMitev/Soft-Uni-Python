import re


current_input = input()

regex = r'\b_([A-Za-z0-9]+)\b'

matches = re.findall(regex, current_input)

print(','.join(matches))