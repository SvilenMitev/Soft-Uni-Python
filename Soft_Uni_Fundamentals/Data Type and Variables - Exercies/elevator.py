number_of_people = int(input())
capacity_of_elevator = int(input())
count = 0
for n in range (number_of_people, 0, -capacity_of_elevator):
    count += 1

print (count)