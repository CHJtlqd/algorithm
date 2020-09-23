import sys

input = sys.stdin.readline

s = input()

result = int(s[0])

for i in range(1,len(s)-1):
    if int(s[i])<=1 or result<=1:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)
