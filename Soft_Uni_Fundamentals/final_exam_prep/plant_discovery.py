number_of_plants = int(input())

garden = {}
for _ in range (number_of_plants) :
    new_plant = input().split("<->")
    plant = new_plant[0]
    rarity = new_plant[1]
    garden[plant] = [rarity, []]
    

while True:
    command = input().split(": ")
    if command == ["Exhibition"]:
        break
    if command[0] == "Rate":
        plant_rathing = command[1].split(" - ")
        plant = plant_rathing[0]
        rathing = plant_rathing[1]
        if plant not in garden:
            print("error")
            continue
        garden[plant][1].append(int(rathing))
        
    elif command[0] == "Update":
        plant_rathing = command[1].split(" - ")
        plant = plant_rathing[0]
        new_rerity = plant_rathing[1]
        if plant not in garden:
            print("error")
            continue
        garden[plant][0] = new_rerity
    elif command[0] == "Reset":
        plant = command[1]
        if plant not in garden:
            print("error")
            continue
        garden[plant][1] = 0
    
print("Plants for the exhibition:")


for key, value in garden.items():
    if value[1] == 0 or len(value[1]) == 0:
        sum_rating = 0
    else:
        sum_rating = sum(value[1]) / len(value[1])
    print(f"- {key}; Rarity: {value[0]}; Rating: {sum_rating:.2f}")
    

    
    