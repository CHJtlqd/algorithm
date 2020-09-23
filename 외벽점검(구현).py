# https://programmers.co.kr/learn/courses/30/lessons/60062
# 순열
# 시계방향으로만 돌아도 해결됨( 원의 길이를 2배로 늘린다고 생각하고 추가될 원소는 n을 더해줌)
# 선택되는 순서에 따라 결과가 달라짐
import sys
from itertools import permutations

input = sys.stdin.readline


def solution(n, weak, dist):
    answer = len(dist) + 1

    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer
