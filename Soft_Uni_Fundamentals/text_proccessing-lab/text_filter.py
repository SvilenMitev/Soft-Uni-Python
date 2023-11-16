banned_words = input().split(", ")
text_input = input()


for i in banned_words:
    if i in text_input:
        text_input = text_input.replace(i, len(i)*"*")
print(text_input)


