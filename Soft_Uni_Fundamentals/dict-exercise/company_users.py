companys_employees_dict = {}

while True:
    current_input = input().split(" -> ")
    if current_input == ["End"]:
        break
    company = current_input[0]
    employee_id = current_input[1]
    if company not in companys_employees_dict:
        companys_employees_dict[company] = []
    if employee_id in companys_employees_dict.get(company):
        continue
    else:
        companys_employees_dict[company].append(employee_id)
next_row = "\n"
for company, employee in companys_employees_dict.items():
    print(f"{company}{next_row}-- {f'{next_row}-- '.join(employee)}")