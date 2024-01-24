row, col = map(int, input().split(","))
matrix = []
total_sum = []

for i in range(row):
    matrix.append(list(map(int, input().split())))
for y in range(col):
    number = 0
    for t in range(row):
        number += matrix[t][y]
    print(number)