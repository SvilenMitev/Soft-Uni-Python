string_input = input()

stack = []

for i in range(len(string_input)):
    if string_input[i] == "(":
        stack.append(i)
    elif string_input[i] == ")":
        print(string_input[stack.pop():i+1])