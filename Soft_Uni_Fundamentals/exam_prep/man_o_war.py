
#To_review
def war_ship_damage(pirate_list, range_one, range_two, damage_done):
    temp_list = []
    for i in (pirate_list[range_one:range_two]):
        current_number = i - damage_done
        temp_list.append(current_number)

    pirate_list[range_one:range_two] = temp_list
    return pirate_list


pirate_ship = input().split('>')
war_ship = input().split('>')

health_capacity = int(input())

while True:
    command = input().split()
    command_type = command[0]
    if command_type == 'Retire':
        break
    elif command_type == 'Fire':
        if int(command[1]) <= len(war_ship) -1:
            current_index = int(command[1])
            damage = int(command[2])
            current_health = int(war_ship[current_index]) - damage
            war_ship[current_index] = war_ship[current_health]
            if any((lambda i: i <= 0)(i) for i in war_ship):
                print("Fire")
                break
    elif command_type == 'Defend':
        if int(command[1]) <= len(pirate_ship) - 1 and int(command[2]) <= len(pirate_ship):
            pirate_ship = war_ship_damage(pirate_ship, int[command[1]], int[command[2]] , int[command[3]])
            if any((lambda i: i <= 0)(i) for i in pirate_ship):
                print("defend")
                break
    elif command_type == 'Repair':
        if int(command[1]) <= len(war_ship) - 1:
            current_index = int(command[1])
            repair_health = int(command[2])
            current_health = int(pirate_ship[current_index]) + repair_health
            if current_health > health_capacity:
                current_health = health_capacity
            pirate_ship[current_index] = pirate_ship[current_health]
            print("repair")
    elif command_type == 'Status':
        percentage_of_capacity = health_capacity * 0.2
        count = lambda x: x in pirate_ship if x <= percentage_of_capacity
        print(f"{count} sections need repair.")







