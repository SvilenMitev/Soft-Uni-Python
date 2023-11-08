inventory_dict = {"shards": 0, "fragments": 0, "motes":0}
legendary_item = ""

while legendary_item == "":
    list_of_items = input().split()
    for i in range(0, len(list_of_items), 2):
        current_value = int(list_of_items[i])
        current_key = list_of_items[i + 1].lower()
        if current_key not in inventory_dict.keys():
            inventory_dict[current_key] = 0
        inventory_dict[current_key] += current_value
        if inventory_dict["shards"] >= 250:
            legendary_item = "Shadowmourne"
            inventory_dict["shards"] -= 250
            break
        if inventory_dict["fragments"] >= 250:
            legendary_item = "Valanyr"
            inventory_dict["fragments"] -= 250
            break
        if inventory_dict["motes"] >= 250:
            legendary_item = "Dragonwrath"
            inventory_dict["motes"] -= 250
            break

print(f"{legendary_item} obtained!")
for keys, value in inventory_dict.items():
        print(f"{keys}: {value}")



