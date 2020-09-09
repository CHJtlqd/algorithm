# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def solution(food_times, k):
    if sum(food_times) < k:
        return -1

    pq = []
    for i in range(len(food_times)):
        # heapq.heappush(list, (우선 순위, 값))
        heapq.heappush(pq, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)
    # 남아있는 시간이 제일 작은 음식을 남아있는 음식의 갯수만큼 뺌
    # 뺀 값은 총 음식을 먹은 시간이 되고 만약 뺀 수와 이전에 먹은 시간
    # 합이 k보다 크면 (k-sum)에서 남은 음식의 수를 나눠 나머지 값을 구함
    while sum_value + ((pq[0][0] - previous) * length) <= k:
        now = heapq.heappop(pq)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(pq, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
food=[4,2,4]
print(solution(food,5))


