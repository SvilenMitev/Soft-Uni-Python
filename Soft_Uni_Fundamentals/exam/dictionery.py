word_and_definitions = input().split(" | ")
word_dict = {}


for i in word_and_definitions:
    command = i.split(": ")
    key = command[0]
    value = command[1]
    if key not in word_dict.keys():
        word_dict[key] = []
    word_dict[key].append(value)

# print(word_dict)

second_string = input().split(" | ")

command = input()

if command == "Test":
    for j in second_string:
        if j in word_dict:
            print(j+":")
            for word in word_dict[j]:
                print(f" -{word}")
        # new_line = "\n"
        # print(f" -{' -'.join(word_dict[j])}")


if command == "Hand Over":
    print(f"{' '.join(word_dict.keys())}")

