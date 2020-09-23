import sys
from collections import deque
import heapq

input = sys.stdin.readline


# https://programmers.co.kr/learn/courses/30/lessons/42891
# 일반 큐로 푸는 문제는 시간초과
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)
    while sum_value + (hq[0][0] - previous) * length <= k:
        now = heapq.heappop(hq)[0]
        sum_value += (now - previous) * length
        previous = now
        length -= 1

    hq.sort(key=lambda x: x[1])
    answer = hq[(k - sum_value) % length][1]
    return answer


print(solution([3, 1, 2], 5))
