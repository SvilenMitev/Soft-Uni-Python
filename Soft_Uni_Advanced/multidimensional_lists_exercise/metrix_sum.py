rows, colms = map(int, input().split())
counter = 0
matrix = []
start = 0
for i in range(rows):
    matrix.append(list(input().split(" ")))
    
for row in range( rows-1):
    for col in range( colms - 1):
        if matrix[row][col] == matrix[row][col + 1] and matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+1][col + 1]:
            counter += 1
        
print(counter)