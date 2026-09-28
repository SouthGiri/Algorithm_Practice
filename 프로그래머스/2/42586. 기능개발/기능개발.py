def solution(progresses, speeds):
    from math import ceil
    answer = []
    tmp = 0
    for idx in range(len(progresses)):
        time = ceil((100 - progresses[idx]) / speeds[idx])
        
        if time > tmp:
            answer.append(1)
            tmp = time
        else:
            answer[-1] += 1
    return answer