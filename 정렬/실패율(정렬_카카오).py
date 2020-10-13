def solution(N, stages):
    answer = []
    arr=[0]*(N+1)
    count=len(stages)
    for num in stages:
        if num>N:
            continue
        arr[num]+=1
    temp=[]
    pre=0
    idx=1
    for i in range(1,len(arr)):

        if pre==count:
            temp.append((0,idx))
            idx+=1
            continue
        temp.append((arr[i]/(count-pre),idx))
        pre+=arr[i]
        idx+=1
    temp.sort(key=lambda x: (-x[0],x[1]))

    answer=list(map(lambda x:x[1],temp))
    print([x[1] for x in temp])
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])