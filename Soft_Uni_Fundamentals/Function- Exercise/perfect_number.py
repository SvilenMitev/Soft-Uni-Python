def perfect_number(number:int):
    list_of_good_numbers = []
    for i in range(1, number):
        if number % i == 0:
            list_of_good_numbers.append(i)
    if number == sum(list_of_good_numbers):
        print ("We have a perfect number!" )
    else:
        print("It's not so perfect." )

intput_number = int(input())
perfect_number(intput_number)
