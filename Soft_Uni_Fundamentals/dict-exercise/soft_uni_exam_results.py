from collections import Counter


exam_results_dict = {}

while True:
    student_input = input().split("-")
    if student_input == ["exam finished"]:
        break
    student_name = student_input[0]
    language = student_input[1]
    if language == "banned":
        exam_results_dict[student_name][1] = "banned"
        continue
    student_score = int(student_input[2])
    if student_name not in exam_results_dict:
        exam_results_dict[student_name] = []
        exam_results_dict[student_name].append(language)
        exam_results_dict[student_name].append(student_score)
    if student_name in exam_results_dict and exam_results_dict[student_name][0] == language and exam_results_dict[student_name][1] < student_score:
        exam_results_dict[student_name][1] = student_score
        exam_results_dict[student_name].append(language)
    elif student_name in exam_results_dict and exam_results_dict[student_name][0] != language:
        exam_results_dict[student_name].append(language)
        exam_results_dict[student_name].append(student_score)
    elif student_name in exam_results_dict and exam_results_dict[student_name][0] == language and exam_results_dict[student_name][1] > student_score:
        exam_results_dict[student_name].append(language)

print("Results:")
for names, points in exam_results_dict.items():
    if "banned" in points:
        continue
    for i in points:
        if  isinstance(i, int):
            print(f"{names} | {i}")


print("Submissions:")
templist = []
for values in exam_results_dict.values():
    for i in values:
        if  i != "banned" and isinstance(i, str):
            templist.append(i)


counted_items = Counter(templist)

# Print the counts
for item, count in counted_items.items():
    print(f"{item} - {count}")









