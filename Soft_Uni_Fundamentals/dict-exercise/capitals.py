countrys_input = input().split(", ")
capitals_input = input().split(", ")

result_dict = {countrys_input[i]: capitals_input[i] for i in range(len(capitals_input))}
for country, capital in result_dict.items():
    print(f"{country} -> {capital}")
