from collections import deque


def move(first, second, board):
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    ret = []

    for m in dir:
        if board[first[0] + m[0]][first[1] + m[1]] == 0 and board[second[0] + m[0]][second[1] + m[1]] == 0:
            ret.append({(first[0] + m[0], first[1] + m[1]), (second[0] + m[0], second[1] + m[1])})

    rotate = [1, -1]
    if first[0] == second[0]:
        for r in rotate:
            if board[first[0] + r][first[1]] == 0 and board[second[0] + r][second[1]] == 0:
                ret.append({(first[0] + r, first[1]), (first[0], first[1])})
                ret.append({(second[0] + r, second[1]), (second[0], second[1])})
    else:
        for r in rotate:
            if board[first[0]][first[1] + r] == 0 and board[second[0]][second[1] + r] == 0:
                ret.append({(first[0], first[1]), (first[0], first[1] + r)})
                ret.append({(second[0], second[1]), (second[0], second[1] + r)})
    return ret


def solution(board):
    answer = 0
    new_board = [[1 for _ in range(len(board) + 2)] for _ in range(len(board) + 2)]

    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []

    q.append([{(1, 1), (1, 2)}, 0])
    visited.append({(1, 1), (1, 2)})

    while q:
        temp = q.popleft()
        dist = temp[1] + 1
        nodes = list(temp[0])

        for m in move(nodes[0], nodes[1], new_board):
            if (len(board), len(board)) in m:
                return dist

            if not m in visited:
                q.append([m, dist])
                visited.append(m)

    return 0
