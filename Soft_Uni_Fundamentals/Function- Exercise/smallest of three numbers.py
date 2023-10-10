def smallest_number(fist,second,third):
    function_list = [fist,second,third]
    result_list = []
    for i in (function_list):
        result_list.append(int(i))
    result = min(result_list)
    return result



first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_number(first_number, second_number, third_number))

