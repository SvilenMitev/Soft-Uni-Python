input_year = int(input())

while True:
    input_year += 1
    str_year = str(input_year)
    if len(set(str_year)) == len(str_year):
        print(input_year)
        break
