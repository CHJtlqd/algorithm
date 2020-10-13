def solution(N):
    if N==1 or N==2:
        return N
    arr=[0]*(N+1)
    arr[1]=1
    arr[2]=2
    for i in range(3,N+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[N]

print(solution(5))