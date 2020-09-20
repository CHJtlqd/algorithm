def solution(new_id):
    answer = ''
    count = 0
    flag = False
    new_id = list(new_id)
    # 1, 2, 3
    for i in range(len(new_id)):
        if new_id[i].isalpha():
            new_id[i] = new_id[i].lower()
        elif new_id[i].isdigit():
            new_id[i] = new_id[i]
        else:
            if new_id[i] == '-' or new_id[i] == '_' or new_id[i]=='.':
                continue
            else:
                new_id[i] = '@'
    print(new_id)
    for i in range(len(new_id)):
        if new_id[i]=='.':
            if flag:
                new_id[i]='@'
            else:
                flag=True
        elif new_id[i]=='@':
            continue
        else:
            flag=False



    # for i in range(len(new_id)):
    for i in range(len(new_id)):
        if new_id[i] != '@':
            answer += new_id[i]

    print(answer)
    # 4
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]

    if len(answer) > 0 and answer[len(answer) - 1] == '.':
        answer = answer[0:-1]
    print(answer)
    # 5
    if len(answer) == 0:
        answer += 'a'
    # 6
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[len(answer) - 1] == '.':
            answer = answer[0:-1]
    elif len(answer) <= 2:  # 7
        temp = answer[len(answer) - 1]
        while len(answer) < 3:
            answer += temp
    print(answer)

    return answer


str = "...A.@..b...C@!#@#!-__-...D123EF"
print(solution(str))
