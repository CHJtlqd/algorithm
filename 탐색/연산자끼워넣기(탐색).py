# boj 14888 연산자끼워넣기
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
commands = list(map(int, input().split()))
# total = sum(commands)
result = -987654321
result_min = int(1e9)


#
# def calc(num1, num2, command):
#     if command == '+':
#         return num1 + num2
#     elif command == '-':
#         return num1 - num2
#     elif command == '*':
#         return num1 * num2
#     elif command == '/':
#         if num1 < 0:
#             return (-num1) // num2 * -1
#         elif num2 < 0:
#             return num1 // (-num2) * -1
#         else:
#             return num1//num2
#
#
# def dfs(command, select=[]):
#     # print(command)
#     # print(select)
#     if len(select) == n-1:
#         global result
#         global result_min
#         temp = calc(numbers[0], numbers[1], select[0])
#         # print(select)
#         index = 1
#         for i in range(2, len(numbers)):
#             temp = calc(temp, numbers[i], select[index])
#             index += 1
#             # print(temp,index)
#
#         result = max(result, temp)
#         result_min = min(result_min, temp)
#         return
#
#     for i in range(len(command)):
#         if command[i] != 0:
#             command[i] -= 1
#             if i == 0:
#                 select.append('+')
#             elif i == 1:
#                 select.append('-')
#             elif i == 2:
#                 select.append('*')
#             elif i == 3:
#                 select.append('/')
#             dfs(command, select)
#             command[i] += 1
#             select.pop(-1)
#
#
# dfs(commands)

def dfs(pre, next, plus, minus, mul, div):
    if next == n:
        global result_min, result
        result_min = min(result_min, pre)
        result = max(result, pre)
        return
    if plus:
        dfs(pre + numbers[next], next + 1, plus - 1, minus, mul, div)
    if minus:
        dfs(pre - numbers[next], next + 1, plus, minus - 1, mul, div)
    if mul:
        dfs(pre * numbers[next], next + 1, plus, minus, mul - 1, div)
    if div:
        dfs(int(pre / numbers[next]), next + 1, plus, minus, mul, div - 1)


dfs(numbers[0], 1, *commands)
print(result)
print(result_min)
