# from itertools import islice

# initial_string = input()
# final_string = ''
# for i in initial_string:
#     if final_string[-1] == '<' :



some_string = input()
strength = 0
finan_string = ""

for index in range(len(some_string)):
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    elif some_string[index] == ">":
        finan_string += some_string[index]
        strength += int(some_string[index + 1])
    else:
        finan_string += some_string[index]

print(finan_string)