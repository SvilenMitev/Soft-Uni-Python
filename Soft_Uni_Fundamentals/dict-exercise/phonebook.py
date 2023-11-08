phonebook_dict = {}
phonebook_input = ''
while True:
    phonebook_input = input()
    if "-" not in phonebook_input:
        break
    list_phonebook = phonebook_input.split("-")
    if list_phonebook[0] not in phonebook_dict:
        phonebook_dict[list_phonebook[0]] = 0
    phonebook_dict[list_phonebook[0]] = list_phonebook[1]

for i in range(int(phonebook_input)):
    searched_name = input()
    if searched_name in phonebook_dict:
        print(f"{searched_name} -> {phonebook_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
