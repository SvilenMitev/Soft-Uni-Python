def lenght(word):
    if len(word) >= 3 and len(word) <= 16:
        return True
    else:
        return False
    

def can_contain_latters(word):
    status_word = True
    for i in word:
        if i.isalpha() or i.isnumeric() or i == "_" or i == "-":
            continue
        else:
            status_word = False
    return status_word

def no_white_spaces (word):
    status_word = True
    for i in word:
        if i == " ":
            status_word = False
    return status_word


def call_func(word):
    if lenght(word) and can_contain_latters(word) and no_white_spaces(word):
        print(word)
    

initial_input = input().split(", ")

for j in initial_input:
    call_func(j)
