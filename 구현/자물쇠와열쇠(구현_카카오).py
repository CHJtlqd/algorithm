def rotate(arr):
    # 배열을 뒤집고 *을 통해 unpacking한 후 zip을 통해 같은 인덱스를 리스트로 묶음
    return list(zip(*arr[::-1]))


def attach(x, y, M, new_rotate,board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j]+=new_rotate[i][j]


def detach(x, y, M, new_rotate,board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= new_rotate[i][j]

def check(board,M,N):
    for i in range(N):
        for j in range(N):
            if board[i+M-1][j+M-1]!=1:
                return False
    return True





def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0]*((M - 1) * 2 + N) for _ in range((M - 1) * 2 + N)]

    for i in range(N):
        for j in range(N):
            board[M-1+i][M-1+j]=lock[i][j]
    new_rotate = key
    for _ in range(4):
        new_rotate = rotate(new_rotate)
        for x in range(M+N-1):
            for y in range(M+N-1):
                attach(x,y,M,new_rotate,board)
                if check(board,M,N):
                    return True
                detach(x,y,M,new_rotate,board)
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
print(key[::-1])
print(list(zip(*key[::-1])))

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))