import sys
from itertools import combinations

n = int(sys.stdin.readline())
board = []
teachers = []
spaces = []
for i in range(n):
    board.append(list(sys.stdin.readline().rsplit()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            spaces.append((i, j))

result = False


# 특정 방향으로 감시를 진행 (학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':  # 학생이 있는 경우
                return True
            if board[x][y] == 'O':  # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':  # 학생이 있는 경우
                return True
            if board[x][y] == 'O':  # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':  # 학생이 있는 경우
                return True
            if board[x][y] == 'O':  # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':  # 학생이 있는 경우
                return True
            if board[x][y] == 'O':  # 장애물이 있는 경우
                return False
            x += 1
    return False


def check():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


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
