import re

destination_string = input()

regex = r"([=|/])([A-Z][A-Za-z]{3,})\1"

matches = re.finditer(regex, destination_string)
final_list = []
points = 0
for match in matches:
    current_word = match.group()
    current_word = current_word.replace("=", "")
    current_word = current_word.replace("/", "")
    final_list.append(current_word)
    points += len(current_word)
print(f"Destinations: {', '.join(final_list)}")
print(f"Travel Points: {points}")