courses_dict = {}

while True:
    students_input = input().split(" : ")
    if students_input == ["end"]:
        break
    courses = students_input[0]
    students = students_input[1]

    if courses not in courses_dict:
        courses_dict[courses] = []
    courses_dict[courses].append(students)
test = '\n'
for coursers, number_of_students in courses_dict.items():
    print(f"{coursers}: {len(number_of_students)}\n-- {f'{test}-- '.join(number_of_students)}")




#     • Print the information about each course in the following format:
# "{course_name}: {registered_students}"
#     • Print the information about each student in the following format:
# "-- {student_name}"