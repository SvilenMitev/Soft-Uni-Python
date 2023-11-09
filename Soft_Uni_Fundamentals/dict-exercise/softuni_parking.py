number_of_inputs = int(input())
parking_dict = {}
for cars_entry in range(number_of_inputs):
    current_car = input().split()
    status = current_car[0]
    user_name = current_car[1]
    if status == "register": plate_number = current_car[2]
    if status == "register" and user_name not in parking_dict:
        parking_dict[user_name] = plate_number
        print(f"{user_name} registered {plate_number} successfully")
    elif status == "register" and user_name in parking_dict:
        print(f"ERROR: already registered with plate number {plate_number}")
    if status == "unregister" and user_name not in parking_dict:
        print(f"ERROR: user {user_name} not found")
    elif status == "unregister" and user_name in parking_dict:
        print(f"{user_name} unregistered successfully")
        del parking_dict[user_name]

for users, plates in parking_dict.items():
    print(f"{users} => {plates}")
