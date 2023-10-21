import math


number_of_students = int(input())
number_of_lectures = int(input())
bonus_point = int(input())
bonus_point_list = []
attendance_list = []
for i in range(number_of_students):
    attendance_per_student = int(input())
    attendance_list.append(attendance_per_student)
    total_bonus = attendance_per_student / number_of_lectures * (5 + bonus_point)
    bonus_point_list.append(total_bonus)

print(f"Max Bonus: {math.ceil(max(bonus_point_list))}.")
print(f"The student has attended {max(attendance_list)} lectures.")
