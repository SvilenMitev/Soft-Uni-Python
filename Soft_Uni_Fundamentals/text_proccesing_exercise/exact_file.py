inital_string = input().split("\\")

word = inital_string[-1].split(".")

final_word = word[0]
extension = word [1]

print(f"File name: {final_word}")
print(f"File extension: {extension}")

data = input().split("\\")
name, extensions = data[-1].split(".")
print(f"File name: {name}")
print(f"File extension: {extensions}")

