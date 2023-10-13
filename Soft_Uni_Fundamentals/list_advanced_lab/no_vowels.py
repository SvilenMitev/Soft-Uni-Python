
text = input()

new_string = lambda text: ''.join([i for i in text if i.lower() not in ('a', 'o', 'u', 'e', 'i')])

result = new_string(text)

print(result)
