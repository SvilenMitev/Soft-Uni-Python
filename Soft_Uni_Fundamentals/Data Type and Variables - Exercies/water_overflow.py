number_of_input = int(input())
total_capacity = 255
count = 0
for i in range(number_of_input):
    liters_of_water = int(input())
    if liters_of_water + count <= total_capacity:
        count += liters_of_water
    else:
        print("Insufficient capacity!" )
print(count)



