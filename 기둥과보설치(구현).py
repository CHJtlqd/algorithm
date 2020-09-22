# https://programmers.co.kr/learn/courses/30/lessons/60061
def solution(n, build_frame):
    answer = []
    board = [[0] * (n + 1) for _ in range(n + 1)]
    for data in build_frame:
        x, y, a, b = data
        # a==0 기둥 a==1 보
        # b==0 삭제 b==1 설치
        if b == 1:
            answer.append([x, y, a])
            if possible(answer):
                continue
            else:
                answer.remove([x, y, a])
        elif b == 0:
            answer.remove([x, y, a])
            if possible(answer):
                continue
            else:
                answer.append([x, y, a])
    answer.sort()
    return answer


def possible(result):
    for data in result:
        x, y, stuff = data
        if stuff == 0:
            if y == 0 or [x, y - 1, 0] in result or [x - 1, y, 1] in result or [x, y, 1] in result:
                continue
            else:
                return False
        elif stuff == 1:
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or (
                    [x - 1, y, 1] in result and [x + 1, y, 1] in result):
                continue
            else:
                return False
    return True
