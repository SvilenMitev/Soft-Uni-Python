inital_string = input().split("\\")

word = inital_string[-1].split(".")

final_word = word[0]
extension = word [1]

print(f"file name:{final_word}")
print(f"File extension:{extension}")

