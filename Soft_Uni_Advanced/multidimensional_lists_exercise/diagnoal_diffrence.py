n = int(input())

matrix = [[int(el) for el in input().split(" ")] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
second = [matrix[r][n - r - 1] for r in range(n)]

result = abs(sum(primary) - sum(second))
print(result)