import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
graph=[]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
# print(graph)
arr=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            arr.append((i, j, graph[i][j], 0))

# print(arr)
arr=sorted(arr,key=lambda x : x[2])
for temp in arr:
    queue.append(temp)

s,x,y=map(int, sys.stdin.readline().split())
time = 0
while queue:
    temp = queue.popleft()
    if temp[3]>=s:
        break
    for i in range(4):
        nx = temp[0]+dx[i]
        ny = temp[1]+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n or graph[nx][ny] != 0:
            continue
        graph[nx][ny]=temp[2]
        queue.append((nx,ny,temp[2],temp[3]+1))
    # print(graph)
print(graph[x-1][y-1])