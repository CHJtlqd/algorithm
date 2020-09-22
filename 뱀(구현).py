# boj 3190 뱀
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

l = int(input())
command = []
for _ in range(l):
    x, c = input().split()
    x = int(x)
    command.append((x, c))

count = 0
snake = deque()
snake.append((1, 1))
dirX = [0, 1, 0, -1]
dirY = [1, 0, -1, 0]
dir = 0
while True:
    temp = snake[0]
    dx = temp[0] + dirX[dir]
    dy = temp[1] + dirY[dir]
    count += 1
    if dx < 1 or dy < 1 or dx > n or dy > n or (dx, dy) in snake:
        break
    if board[dx][dy] == 1:
        board[dx][dy] = 0
        snake.appendleft((dx, dy))
    else:
        snake.appendleft((dx, dy))
        snake.pop()
    if len(command) > 0 and count == command[0][0]:
        if command[0][1] == 'L':
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4
        command.pop(0)

print(count)
