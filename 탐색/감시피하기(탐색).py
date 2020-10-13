# boj 18428 감시피하기
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

board = []
spaces = []
teachers = []

for i in range(n):
    board.append(list(input().rsplit()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            spaces.append((i, j))


def watch(x, y, i):
    # True 학생 발견, False 막혀있거나 학생이 없음
    if i == 0:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            x -= 1
    elif i == 1:
        while x < n:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            x += 1
    elif i == 2:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            y -= 1
    elif i == 3:
        while y < n:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            y += 1
    return False


def check():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


result = False
for temp in combinations(spaces, 3):
    for x, y in temp:
        board[x][y] = 'O'
    if not check():
        result = True
        break

    for x, y in temp:
        board[x][y] = 'X'

if result:
    print('YES')
else:
    print('NO')
