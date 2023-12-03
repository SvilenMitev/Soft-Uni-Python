import re

number_of_strings = int(input())

regex = r"![A-Z][a-z]{2,}!:\[[A-Za-z]{8,}\]"
for i in range(number_of_strings):
    word = input()
    match = re.findall(regex, word)
    if match:
        string  = match[0].split(":")
        command = string[0]
        command = command[1:-1]
        word = string[1]
        word_list = []
        for i in word:
            if i.isalpha():
                word_list.append(str(ord(i)))
        print(f"{command}: {' '.join(word_list)}")

    else:
        print("The message is invalid")
        
