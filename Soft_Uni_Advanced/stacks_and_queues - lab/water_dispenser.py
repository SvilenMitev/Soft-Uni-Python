from collections import deque
water_in_dispenser = int(input())
list_of_people = deque([])
while True:
    people_names = input()
    if people_names == "Start":
        break
    list_of_people.append(people_names)

while True:
    command = input()
    if command == "End":
        break
    elif command[0] == "r":
        water = (command[-2:])
        water_in_dispenser += int(water)
    elif command.isdigit:
        if water_in_dispenser >= int(command):
            print(f"{list_of_people.popleft()} got water") 
            water_in_dispenser -= int(command)
        else:
            print(f"{list_of_people.popleft()} must wait") 
print(f"{water_in_dispenser} liters left")
    