def solution(histogram):
    answer = 0
    start = 0
    end = len(histogram) - 1
    while start < end:
        rect = (end - start - 1)
        if histogram[start] >= histogram[end]:
            rect = rect * histogram[end]
            end -= 1
        else:
            rect = rect * histogram[start]
            start += 1
        answer=max(answer,rect)
    return answer

histgram=[6, 5, 7, 3, 4, 2]

print(solution(histgram))