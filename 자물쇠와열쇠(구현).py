import sys

input = sys.stdin.readline

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[i + M - 1][j + M - 1] != 1:
                return False
    return True


def attach(x, y, M, new_rotate, board):
    for i in range(M):
        for j in range(M):
            board[i + x][j + y] += new_rotate[i][j]


def dettach(x, y, M, new_rotate, board):
    for i in range(M):
        for j in range(M):
            board[i + x][j + y] -= new_rotate[i][j]


def rotate(arr):
    return list(zip(*arr[::-1]))

def solution(key, lock):
    N = len(lock)
    M = len(key)
    board = [[0] * ((M - 1) * 2 + N) for _ in range((M - 1) * 2 + N)]
    for i in range(N):
        for j in range(N):
            board[i + (M - 1)][j + (M - 1)] = lock[i][j]

    new_rotate = key
    for _ in range(4):
        new_rotate = rotate(new_rotate)
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                attach(i, j, M, new_rotate, board)
                if check(board, M, N):
                    return True
                dettach(i, j,M, new_rotate, board)
    return False





key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))
