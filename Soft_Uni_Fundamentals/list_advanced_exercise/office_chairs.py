number_of_rooms = int(input())
free_chairs_count = 0
not_enough_space = False
room_number = 0
error_count = 0
for i in range(number_of_rooms):
    room_number += 1
    number_of_people = input().split()
    room_status = len(number_of_people[0]) - int(number_of_people[1])
    if room_status >= 0:
        free_chairs_count += room_status
    else:
        room_status = abs(room_status)
        not_enough_space = True
    if not_enough_space:
        error_count += 1
        print(f"{room_status} more chairs needed in room {room_number}")
if error_count == 0:
    print(f"Game On, {free_chairs_count} free chairs left")
