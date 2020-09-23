# boj 15686 치킨배달
import sys
from itertools import combinations
from collections import deque

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
# result = int(1e9)
# for data in list(combinations(chickens, m)):
#     length = 0
#     for house in houses:
#         distance_min = int(1e9)
#         for chicken in data:
#             distance_min = min(distance_min, abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
#         length += distance_min
#     result = min(result, length)

# print(result)
distances = []
for house in houses:
    temp = []
    for chicken in chickens:
        temp.append(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
    distances.append(temp)
distances = list(zip(*distances))


def check_distance(select=[], index=-1):
    if len(select) == m:
        values = list(zip(*select))
        w = 0
        for value in values:
            w += min(value)
        return w
    if index == len(distances):
        return int(1e9)
    result = int(1e9)
    for i in range(index + 1, len(distances)):
        select.append(distances[i])
        result = min(result, check_distance(select, i))
        select.pop(-1)

    return result


print(check_distance())

# import sys
#
# input = sys.stdin.readline
#
# n, m = list(map(int, input().strip().split()))
# grid = []
# for _ in range(n):
#     grid.append(list(map(int, input().strip().split())))
# house = []
# chicken = []
# for i in range(n):
#     for j in range(n):
#         v = grid[i][j]
#         if v == 1:
#             house.append([i, j])
#         elif v == 2:
#             chicken.append([i, j])
# distance = []
# for h in house:
#     h_x, h_y = h
#     h_l = []
#     for c in chicken:
#         c_x, c_y = c
#         h_l.append(abs(h_x - c_x) + abs(h_y - c_y))
#     distance.append(h_l)
#     # print(distance)
# distance = list(zip(*distance))
#
# print(distance)
# def check(select=[], index=-1):
#     if len(select) == m:
#         values = list(zip(*select))
#         print(values)
#         w = 0
#         for v in values:
#             w += min(v)
#         return w
#     if index == len(distance):
#         return 999999
#     # 순서는 상관 없음
#     ret = 99999999
#     for i in range(index + 1, len(distance)):
#         select.append(distance[i])
#         ret = min(ret, check(select, i))
#         select.pop(-1)
#     return ret
#
#
# print(check())
