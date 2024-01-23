
row, col = map(int, input().split(", "))
matrix = []
total_sum = 0
for i in range(row):
    matrix.append(list(map(int, input().split(", "))))
    total_sum += sum(matrix[i])
print(total_sum)
print(matrix)
    