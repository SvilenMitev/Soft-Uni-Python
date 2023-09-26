lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_repair_price = 0
sword_repair_price = 0
shield_repair_price = 0
armor_repair_price = 0
count = 0

for n in range(1, lost_fight_count+1):
    if n % 2 == 0:
        helmet_repair_price += helmet_price
    if n % 3 == 0:
        sword_repair_price += sword_price
    if n % 3 == 0 and n % 2 == 0:
        shield_repair_price += shield_price
        count += 1
    if count == 2:
        armor_repair_price += armor_price
        count = 0

total_price = helmet_repair_price + sword_repair_price + shield_repair_price + armor_repair_price

print(f"Gladiator expenses: {total_price:.2f} aureus")

