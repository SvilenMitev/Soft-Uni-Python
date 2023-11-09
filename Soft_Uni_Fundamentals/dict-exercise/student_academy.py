students_grade = {}

number_of_students = int(input())

for _ in range(number_of_students):
    student_name = input()
    grade = float(input())
    if student_name not in students_grade:
        students_grade[student_name] = []
    students_grade[student_name].append(grade)

for students, grades in students_grade.items():
    avg_grades = sum(grades)/len(grades)
    if avg_grades >= 4.50:
        print(f"{students} -> {avg_grades:.2f}")