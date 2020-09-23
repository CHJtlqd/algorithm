array = [7, 5, 2, 3, 1, 4, 12, 4, 3]


# 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하여 시간 측면에서 더 비효율적이나 직관적이다.
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
