# boj 15686 치킨배달
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0] * (n + 1) for _ in range(n + 1)]
houses = []
chickens = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        board[i + 1][j + 1] = row[j]
        if board[i + 1][j + 1] == 2:
            chickens.append((i + 1, j + 1))
        elif board[i + 1][j + 1] == 1:
            houses.append((i + 1, j + 1))
result = n * n
for data in list(combinations(chickens, m)):
    length = 0
    for chicken in data:
        for house in houses:
            length += abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
    result = min(result, length)

print(list(combinations(chickens, m)))
print(result)