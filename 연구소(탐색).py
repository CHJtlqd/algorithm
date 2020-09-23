# https://www.acmicpc.net/problem/14502
import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
hole = []
virus = []
count = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        graph[i][j] = temp[j]
        if temp[j] == 0:
            hole.append((i, j))
            count += 1
        elif temp[j] == 2:
            virus.append((i, j))
result = 0
dirX = [-1, 1, 0, 0]
dirY = [0, 0, -1, 1]
def dfs(cnt,x,y):
    if cnt==3:
        #print(graph)
        tcount=count-3
        tgraph=copy.deepcopy(graph)
        q = deque()
        global result
        for v in virus:
            q.append(v)
        while q:
            temp = q.popleft()
            for i in range(4):
                dx = temp[0] + dirX[i]
                dy = temp[1] + dirY[i]
                if dx < 0 or dy < 0 or dx >= n or dy >= m or tgraph[dx][dy] != 0:
                    continue
                q.append((dx, dy))
                tgraph[dx][dy] = 2
                tcount -= 1
                if tcount < result:
                    return
        result=max(result,tcount)
        return
    for i in range(x,n):
        k=y if i==x else 0
        for j in range(k,m):
            if graph[i][j]==0:
                graph[i][j]=1
                dfs(cnt+1,i,j+1)
                graph[i][j]=0
dfs(0,0,0)
# for data in list(combinations(hole, 3)):
#     tgraph=copy.deepcopy(graph)
#     tcount=count
#     for x, y in data:
#         tgraph[x][y] = 1
#         tcount-=1
#     q = deque()
#     for v in virus:
#         q.append(v)
#     while q:
#         temp = q.popleft()
#         for i in range(4):
#             dx = temp[0] + dirX[i]
#             dy = temp[1] + dirY[i]
#             if dx < 0 or dy < 0 or dx >= n or dy >= m or tgraph[dx][dy] != 0:
#                 continue
#             q.append((dx, dy))
#             tgraph[dx][dy] = 2
#             tcount -= 1
#             if tcount<result:
#                 break
#     # print("\n".join(map(str,tgraph)))
#     # print()
#     result = max(result, tcount)


print(result)
