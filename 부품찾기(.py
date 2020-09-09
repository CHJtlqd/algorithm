n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 집합 자료형의 in 을 사용하여 문제를 해결 가능

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print("Yes", end=' ')
    else:
        print("No", end=' ')
