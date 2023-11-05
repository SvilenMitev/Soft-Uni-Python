count_of_word = int(input())

synonyms_dict = {}

for i in range(count_of_word):
    word_input = input()
    synonyms_input = input()
    if word_input not in synonyms_dict:
        synonyms_dict[word_input] = []
    synonyms_dict[word_input].append(synonyms_input)

for j in synonyms_dict:
    print(f"{j} - {', '.join(synonyms_dict[j])}")