import sys
input = sys.stdin.readline


def solution(flowers):
    answer = 0
    flowers.sort(key=lambda x:x[0])
    arr = [False]*(flowers[len(flowers)-1][1]+1)
    for start,end in flowers:
        for start in range(start,end):
            arr[start]=True
    for i in range(len(arr)):
        if arr[i]:
            answer+=1

    return answer

print(solution(flowers=[[3, 4],[4, 5], [6, 7], [8, 10]]))