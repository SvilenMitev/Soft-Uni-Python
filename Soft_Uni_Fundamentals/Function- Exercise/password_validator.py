def password_validator(word:str):
    error_counter = 0
    if len(word) < 6 or len(word) > 10:
        error_counter +=1
        print("Password must be between 6 and 10 characters")
    if word.isalnum():
        pass
    else:
        error_counter += 1
        print("Password must consist only of letters and digits")
    count_of_digits = 0
    for i in (word):
        if i.isdigit():
            count_of_digits += 1
    if count_of_digits < 2:
        error_counter += 1
        print("Password must have at least 2 digits")
    if error_counter == 0:
        print("Password is valid")



login = input()
password_validator(login)