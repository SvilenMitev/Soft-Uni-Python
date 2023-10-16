def reverse(value:int):
    if value <= 0:
        print("Done!")
        return
    else:
        for i in range(value):
            print("\U0001f600", end='')
        print()
        reverse(value-1)
reverse(10)
