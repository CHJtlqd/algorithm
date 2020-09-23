import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
arr = [0] * (m + 1)
for i in data:
    arr[i] += 1

result = 0

# for i in range(1, m):
#    result += arr[i] * sum(arr[(i + 1):])
for i in range(1, m + 1):
    n -= arr[i]
    result += n * arr[i]
print(result)
