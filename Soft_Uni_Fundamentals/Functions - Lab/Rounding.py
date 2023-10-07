def round_list(def_list):
    new_list = []
    for i in def_list:
        new_list.append(round(float(i)))
    return new_list

input_list = input().split()
rounded_list = round_list(input_list)
print(rounded_list)
