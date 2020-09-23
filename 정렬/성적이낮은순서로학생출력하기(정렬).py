n = int(input())
array=[]
for _ in range(n):
    data=input().split()
    array.append((data[0],int(data[1])))

array = sorted(array, key=lambda x:x[1])

print(*list(zip(*array))[0])