fundamentals = {}
basics = {}
last_input = ''
while True:
    students_input = input()
    if (":") not in students_input:
        last_input = students_input
        break

    students_id = students_input.split(":")
    if students_id[2] == 'fundamentals':
        fundamentals[students_id[0]] = students_id[1]
    elif students_id[2] == 'programming basics':
        basics[students_id[0]] = students_id[1]

if last_input == 'fundamentals':
    for key, value in fundamentals.items():
        print(f"{key} - {value}")
else:
    for key, value in basics.items():
        print(f"{key} - {value}")


#revurting the key and the value possition to keep unique ids
# fundamentals = {}
# basics = {}
# last_input = ''
# while True:
#     students_input = input()
#     if (":") not in students_input:
#         last_input = students_input
#         break
#
#     students_id = students_input.split(":")
#     if students_id[2] == 'fundamentals':
#         fundamentals[students_id[1]] = students_id[0]
#     elif students_id[2] == 'programming basics':
#         basics[students_id[1]] = students_id[0]
#
# if last_input == 'fundamentals':
#     for value, key in fundamentals.items():
#         print(f"{key} - {value}")
# else:
#     for value, key in basics.items():
#         print(f"{key} - {value}")



#working code

# list_students = []
# course_to_search = ''
#
# while True:
#     input_line = input()
#
#     if ":" not in input_line:
#         course_to_search = input_line
#         break
#
#     name, ID, course = input_line.split(":")
#     list_students.append({"name": name, "ID": ID, "course": course})
#
# for current_student in list_students:
#     if course_to_search.startswith(current_student['course'][0:5]):
#         print(f"{current_student['name']} - {current_student['ID']}")