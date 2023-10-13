def palindrome_list(palindrome_list:list):
    list_of_palindromes = []
    for palindrome in palindrome_list:
        if palindrome == palindrome[::-1]:
            list_of_palindromes.append(palindrome)
    return list_of_palindromes


input_string = input().split()
input_palindrome = input()
count_of_palindrome = palindrome_list(input_string).count(input_palindrome)


print(f"{palindrome_list(input_string)}\nFound palindrome {count_of_palindrome} times")
