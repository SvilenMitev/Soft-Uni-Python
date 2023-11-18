import re

regex = r"\b([0-9]{2})([-./])([A-Z][a-z]{2})\2([0-9]{4})"

current_input = input()

maches = re.findall(regex, current_input)

for i in maches:
    day = i[0]
    month = i[2]
    year = i[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")

