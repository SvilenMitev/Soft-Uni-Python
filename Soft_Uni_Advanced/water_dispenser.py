from collections import deque
water_in_dispenser = int(input())
list_of_people = ([])
while True:
    people_names = input()
    if people_names == "Start":
        break
    list_of_people.append(people_names)
while True:
    command = input()
    if command == "End":
        break
    if isdigit(command):    