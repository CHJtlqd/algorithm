def solution(play_time, adv_time, logs):
    answer = ''
    if play_time == adv_time:
        return "00:00:00"
    for i in range(len(logs)):
        temp = logs[i].split('-')
        logs[i] = (temp[0], temp[1])
    logs = sorted(logs, key=lambda x: x[0])
    print(logs)
    part = []
    start = logs[0][0].split(':')
    end = adv_time.split(':')
    temp=[0]
    for i in range(1, len(logs)):
        if logs[i][0]<logs[i-1][0]:
            temp.append(i)
        

    return answer

def time_add(start, end):
    shh = start[0]
    smm = start[1]
    sss = start[2]

    ehh = end[0]
    emm = end[1]
    ess = end[2]



play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))
