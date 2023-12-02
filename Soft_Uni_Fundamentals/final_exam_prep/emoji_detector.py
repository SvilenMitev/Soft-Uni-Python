import re

emojis = input()
regex = r"[\:]{2}[A-Z][a-z]{2,}[\:]{2}|[*]{2}[A-Z][a-z]{2,}[*]{2}"
regex_numbers = r"\d"

matches = re.findall(regex, emojis)
numbers = re.findall(regex_numbers, emojis)
cool_number = 1
for i in numbers:
    cool_number *= int(i)


print(f"Cool threshold: {cool_number}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for j in matches:
    ascii_values = [ord(char) for char in j]
    if sum(ascii_values) >= cool_number:
        print(j)