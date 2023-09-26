number = int(input())

for n in range(97, 97+number):
    for m in range(97, 97+number):
        for i in range(97, 97 + number):
            print (f"{chr(n)}{chr(m)}{chr(i)}")