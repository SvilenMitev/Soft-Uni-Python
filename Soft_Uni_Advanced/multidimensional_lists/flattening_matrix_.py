from collections import deque

row = int(input())
matrix = []
final_list = []
for i in range(row):
    matrix.append(deque(map(int, input().split(", "))))
    
for y in range(row):
    while len(matrix[y]) > 0:
        final_list.append(matrix[y].popleft())
print(final_list)