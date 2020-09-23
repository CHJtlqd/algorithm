from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True
    while queue:
        temp = queue.popleft()
        if temp[0] == n - 1 and temp[1] == m - 1:
            return temp[2]
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0 or visited[nx][ny]:
                continue

            queue.append((nx, ny, temp[2] + 1))
            visited[nx][ny] = True
    return temp[2]


print(bfs(0, 0)+1)
