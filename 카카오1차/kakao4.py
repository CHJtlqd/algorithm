#플로이드 와샬

def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j]=0

    for data in fares:
        i,j,k= data
        graph[i][j]=k
        graph[j][i]=k


    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    answer=graph[s][a]+graph[s][b]
    for i in range(1,n+1):
        if graph[s][i]==INF or graph[i][a]==INF or graph[i][b]==INF:
            continue
        answer=min(answer,graph[s][i]+graph[i][a]+graph[i][b])

    return answer

n=6
s=4
a=6
b=2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n,s,a,b,fares))