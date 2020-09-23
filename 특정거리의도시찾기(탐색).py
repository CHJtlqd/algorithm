import sys
from collections import deque
import time
input = sys.stdin.readline
start = time.time()
# n, m, k, x = map(int, input().split())
#
# arr = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     start, end = map(int, input().split())
#     arr[start].append(end)
#
# dist = [0] * (n + 1)
# q = deque([x])
# while q:
#     start = q.popleft()
#     for temp in arr[start]:
#         if dist[temp] == 0:
#             dist[temp] = 1 + dist[start]
#             q.append(temp)
#
# check = False
# for i in range(len(dist)):
#     if dist[i] == k:
#         check=True
#         print(i)
# if check == False:
#     print(-1)




def main():
    n, m, k, x = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        edge[a].append(b)

    dist[x] = 0
    q = deque([x])
    f = False
    while q:
        l = len(q)
        for _ in range(l):
            tmp = q.popleft()
            now = dist[tmp]
            if now == k:
                f = True
                break
            for nxt in edge[tmp]:
                if dist[nxt]:
                    continue
                dist[nxt] = now+1
                q.append(nxt)
        if f:
            break
    res = []
    for i in range(1, n+1):
        if dist[i] == k:
            res.append(i)
    print('\n'.join(map(str, res)) if res else -1)

if __name__=='__main__':
    main()
    print(time.time() - start)