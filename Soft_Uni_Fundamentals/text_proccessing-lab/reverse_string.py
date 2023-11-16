

while True:
    current_input = input()
    if current_input == "end":
        break
    reversed_input = current_input[::-1]
    print(f"{current_input} = {reversed_input}")

