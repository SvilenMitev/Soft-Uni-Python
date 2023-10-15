maximum_number = int(input())
list_of_electrons = []

for i in range(1,maximum_number+1):
    full_shell = 2*i**2
    if sum(list_of_electrons) + full_shell < maximum_number:
        list_of_electrons.append(full_shell)
    elif sum(list_of_electrons) < maximum_number:
        list_of_electrons.append(maximum_number-sum(list_of_electrons))
    else:
        break
print(list_of_electrons)
