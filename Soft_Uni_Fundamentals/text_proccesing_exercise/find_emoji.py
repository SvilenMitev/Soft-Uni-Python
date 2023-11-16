initial_string = input().split(":")
final_list = []
for i in initial_string:
    emoji_symbol = i[0]
    final_list.append(emoji_symbol)
for j in final_list:
    if j == final_list[0]:
        continue
    print(f":{j}")

