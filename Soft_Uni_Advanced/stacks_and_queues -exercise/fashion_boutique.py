list_of_clothes = [int(x) for x in input().split()]

size_of_rack = int(input())
rack_counter = 0

while True:
    rack_counter += 1
    current_load = 0
    if len(list_of_clothes) == 0:
        break
    while True:
        if len(list_of_clothes) == 0:
            break
        current_number = list_of_clothes.pop()
        if size_of_rack > current_load + current_number:
            current_load += current_number
        else:
            break

    
print(rack_counter)