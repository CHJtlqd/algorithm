import sys

input = sys.stdin.readline

s = input()
countzero, countone = 0, 0

if s[0] == '0':
    countone += 1
else:
    countzero += 1
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if s[i] == '1':
            countzero += 1
        else:
            countone += 1

print(min(countone, countzero))
