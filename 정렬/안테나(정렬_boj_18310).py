import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
# 0 1 2 3 - 4/2=2
# 0 1 2 3 4 - 5/2 =2

if len(arr) % 2 == 0:
    index1 = len(arr) // 2
    index2 = index1 - 1
    sum1, sum2 = 0, 0
    for num in arr:
        sum1 += abs(arr[index1] - num)
    for num in arr:
        sum2 += abs(arr[index2] - num)
    if sum2 <= sum1:
        print(arr[index2])
    else:
        print(arr[index1])
else:
    print(arr[len(arr) // 2])
