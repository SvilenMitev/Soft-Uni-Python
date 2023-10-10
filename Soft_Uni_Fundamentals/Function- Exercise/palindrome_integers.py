def palindrome_integers(list_of_numbers:list):
    for i in (list_of_numbers):
        if i == i[::-1]:
            print("True")
        else:
            print("False")


string_input = input().split(", ")
palindrome_integers(string_input)