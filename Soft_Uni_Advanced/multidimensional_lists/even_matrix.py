rows = int(input())
matrix = []

for i in range(rows):
    row = list(map(int, input().split(",")))
    matrix.append([num for num in row if num % 2 == 0])
    
print(matrix)
