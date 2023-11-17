import re
name = input()
regex = '\\b[A-Z][a-z]+[ ]{1}[A-Z][a-z]+\\b'
matches = re.findall(regex, name)
print(" ".join(matches))