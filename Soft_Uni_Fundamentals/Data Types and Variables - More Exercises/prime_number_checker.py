number = int(input())

if number > 1:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("True")
    else:
        print("False")
else:
    print("False")
