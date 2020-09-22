import sys

input = sys.stdin.readline

data = list(input()[:-1])
data_str = []
data_digit = 0
for x in data:
    if x.isalpha():
        data_str.append(x)
    else:
        data_digit += int(x)
data_str.sort()
print("".join(data_str) + str(data_digit))
