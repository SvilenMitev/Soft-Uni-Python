# import re


# initial_input = input()

# regex = r'([#|\|])([A-Za-z\s]+)\1[0-9]{2}\/[0-9]{2}\/[0-9]{2}\1[0-9]{0,10000}\1' 

# matches = re.findall(regex, initial_input)

# for match in matches:
#     name = match[1]
#     date = match[2]
#     number = match[3]
#     print(f'|{name}|{date}|{number}|')

import re

initial_input = input()

# Adjusted regex to capture the desired pattern
regex = r'([#|\|])([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1'

matches = re.findall(regex, initial_input)
food = 0
for match in matches:
    food += int(match[3])
days = food // 2000

print(f"You have food to last you for: {days} days!")

for result in matches:
    print(f"Item: {result[1]}, Best before: {result[2]}, Nutrition: {result[3]}")


