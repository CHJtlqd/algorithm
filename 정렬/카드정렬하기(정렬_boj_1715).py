import sys
import heapq
input = sys.stdin.readline

n=int(input())
hq=[]
for _ in range(n):
    heapq.heappush(hq,int(input()))
sum=0
while len(hq)>1:
    num1=heapq.heappop(hq)
    num2=heapq.heappop(hq)
    sum+=num1+num2
    heapq.heappush(hq,num1+num2)

print(sum)