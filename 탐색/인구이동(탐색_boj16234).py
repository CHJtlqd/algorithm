# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N, L, R = map(int, input().rsplit())
# board = []
#
# for _ in range(N):
#     board.append(list(map(int, input().rsplit())))
#
# dirX = [-1, 1, 0, 0]
# dirY = [0, 0, -1, 1]
# result = 0
#
#
# def check_bfs(i, j, visited):
#     q = deque()
#     visited[i][j] = True
#     q.append((i, j))
#     team = []
#     while q:
#         x, y = q.popleft()
#         team.append((x, y))
#         for i in range(4):
#             dx = x + dirX[i]
#             dy = y + dirY[i]
#             if dx < 0 or dy < 0 or dx >= N or dy >= N or visited[dx][dy]:
#                 continue
#             calc = abs(board[x][y] - board[dx][dy])
#             if calc >= L and calc <= R:
#                 q.append((dx, dy))
#                 visited[dx][dy] = True
#     if len(team) == 1:
#         return 0
#     #print(team)
#     sum_node = 0
#     count = len(team)
#
#     for x, y in team:
#         sum_node += board[x][y]
#     sum_node = sum_node // count
#     for x, y in team:
#         board[x][y] = sum_node
#     return 1
#
#
# while True:
#     visited = [[False] * N for _ in range(N)]
#     calc = 0
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 calc += check_bfs(i, j, visited)
#     if calc == 0:
#         break
#     result += 1
#
# print(result)

import sys
from collections import deque

input = sys.stdin.readline

# N,L,R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N*N)을 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x,y)의 위치와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x, y))
    # bfs를 위한 큐 자료구조 정리
    q = deque()
    q.append((x, y))
    union[x][y] = index  # 현재 연합의 번호 할당
    summary = graph[x][y]  # 현재 연합의 전체 인구 수
    count = 1  # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이계산
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count


total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:  # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

print(total_count)
