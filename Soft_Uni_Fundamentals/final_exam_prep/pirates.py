citys_dict = {}

while True:
    target_city = input().split("||")
    if target_city[0] == 'Sail':
        break
    city = target_city[0]
    population = int(target_city[1])
    gold = int(target_city[2])
    if city not in citys_dict.keys():
        citys_dict[city] = [population, gold]
    elif city in citys_dict.keys():
        citys_dict[city][0] += population
        citys_dict[city][1] += gold

while True:
    command = input().split("=>")
    if command[0] == "End":
        break
    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        citys_dict[town][0] -= people
        citys_dict[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if citys_dict[town][0] <= 0 or citys_dict[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del citys_dict[town]
    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        citys_dict[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {citys_dict[town][1]} gold.")

if len(citys_dict) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(citys_dict)} wealthy settlements to go to:")
    for keys, values in citys_dict.items():
        print(f"{keys} -> Population: {values[0]} citizens, Gold: {values[1]} kg")
