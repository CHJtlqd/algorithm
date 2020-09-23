import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x.sort()
result = 0
max = x[0]
count = 0
for i in x:
    count += 1
    if max < i:
        max = i

    if count == max:
        result += 1
        count = 0
        max=-1

print(result)
