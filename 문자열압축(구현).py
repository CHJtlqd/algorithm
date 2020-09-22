# https://programmers.co.kr/learn/courses/30/lessons/60057
import sys

input = sys.stdin.readline


def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        temp = s[0:step]
        compressed = ""
        count = 1
        for i in range(step, len(s), step):
            if temp == s[i:i + step]:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + temp
                    count = 1
                    temp = s[i:i + step]
                else:
                    compressed += temp
                    count = 1
                    temp = s[i:i + step]
        if count > 1:
            compressed += str(count) + temp
        else:
            compressed += temp
        answer = min(answer, len(compressed))
    return answer


print(solution("aaaabbbb"))
