n = int(input())

def upper_part(n):
    for i in range(n):
        print(" " * (n-1-i) + "* " * (1*i+1))
        
def bottom_part(n):
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "* " * (1*i))
upper_part(n)
bottom_part(n)