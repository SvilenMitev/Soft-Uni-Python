import re

initial_string = input()

pattern = r'^[+359]+[ ][2][ ][0-9]{3}[ ][0-9]{4} |^[+359]+[-][2][-][0-9]{3}[-][0-9]{4}'
matches = re.findall(pattern, initial_string)

print(", ".join(matches))

# import re

# initial_string = input()

# pattern = r'\b[+][359]+[ -/][2][ -/][0-9]{3}[ -/][0-9]{4}\b'
# matches = re.findall(pattern, initial_string)

# print(", ".join(matches))



# import re


# inital_string = input()

# patern = r'([+][359]+)([ -])([2]\2[0-9]{3})\2([0-9]{4})\b'
# match = re.findall(patern, inital_string)

# print(", ".join(match))



# import re

# number = input()
# pattern = "\\b+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\\b"
# matches = re.findall(pattern, number)

# print(", ".join(matches))