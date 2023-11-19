import re

regex = r'([w]{3}\.[A-Za-z\-0-9]+(\.[a-z]+)+)'

current_input = input()

while current_input:
    match = re.finditer(regex, current_input)
    if match:
        for i in match:
            print(i.group())
    current_input = input()