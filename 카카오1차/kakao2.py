from itertools import combinations

def solution(orders, course):
    answer = []
    count=[]
    result=[]
    maxOrder=[]
    for i in course:
        for data in orders:
            temp =list(data)
            comb = combinations(temp,i)
            for order in comb:
                order = sorted(order)
                if order in answer:
                    count[answer.index(order)]+=1
                else:
                    count.append(1)
                    answer.append(order)

            # 가장 큰 수 두개를 넣어줌
        if len(answer)==0:
            continue
        maxOrder = sorted(list(zip(answer,count)), key= lambda x : -x[1])
        print(maxOrder)
        answer.clear()
        count.clear()
        maxNum=maxOrder[0][1]
        if maxNum < 2:
            continue
        result.append(''.join(maxOrder[0][0]))
        for i in range(1,len(maxOrder)):
            if maxNum==maxOrder[i][1]:
                result.append(''.join(maxOrder[i][0]))
            else:
                break


    return sorted(result)
orders=["XYZ", "XWY", "WXA"]
course=[2,3,4]

print(solution(orders,course))