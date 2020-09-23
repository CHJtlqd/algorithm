import sys

input = sys.stdin.readline

s = input()

sum_left = 0
sum_right = 0
for i in range(len(s) // 2):
    sum_left += int(s[i])
    sum_right += int(s[len(s) - (i + 2)])

print("LUCKY" if sum_right == sum_left else "READY")
