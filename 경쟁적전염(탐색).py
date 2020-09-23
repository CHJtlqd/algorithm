# boj 18405 경쟁적 전염
import sys
import heapq
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
board = [[0] * n for _ in range(n)]
virues = []
for i in range(n):
    for j, l in enumerate(map(int, input().split())):
        board[i][j] = l
        if l != 0:
            virues.append((l, i, j,0))
virues.sort(key=lambda x: x[0])
virues = deque(virues)
s, x, y = map(int, input().split())

while virues:
    # print(virues)
    num, tempx, tempy,time = virues.popleft()
    if time >=s:
        break

    if tempx == x-1 and tempy == y-1:
        break
        #print(tempx,tempy)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ddx = tempx + dx
        ddy = tempy + dy

        #print(ddx,ddy)
        if ddx < 0 or ddy < 0 or ddx >= n or ddy >= n or board[ddx][ddy] != 0:
            continue
        board[ddx][ddy] = num
        virues.append((num, ddx, ddy,time+1))

# print("\n".join(map(str, board)))
print(board[x - 1][y - 1])
