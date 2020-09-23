def possible(answer):
    for x,y,stuff in answer:
        if stuff==0:
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            else:
                return False
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    result=[]
    for data in build_frame:
        x,y,stuff,operate=data
        if operate==1:
            result.append([x,y,stuff])
            if not possible(result):
                result.remove([x,y,stuff])
        else:
            result.remove([x,y,stuff])
            if not possible(result):
                result.remove([x,y,stuff])

    return sorted(result)


print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
