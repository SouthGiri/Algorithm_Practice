clock = '09:00'

def tick_tock(interval):
    global clock 
    
    hour, minute = int(clock[:2]), int(clock[3:])
    minute += interval
    if minute >= 60:
        hour += (minute // 60)
        minute = minute % 60
    
    hour, minute = str(hour), str(minute)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    
    clock = hour + ':' + minute

def minus_one(cur):
    hour, minute = int(cur[:2]), int(cur[3:])
    
    if minute == 0:
        hour -= 1
        minute = 59
    else:
        minute -= 1
    
    hour, minute = str(hour), str(minute)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    
    return hour + ':' + minute

def solution(n, t, m, timetable):
    answer = ''
    
    timetable.sort()
    
    for _ in range(n):
        boarding = 0
        
        for crew in timetable:
            if crew <= clock:
                boarding += 1
                
            if boarding == m:
                answer = minus_one(timetable[:boarding][-1])
                break
        else:
            answer = clock    
        
        timetable = timetable[boarding:]
        
        tick_tock(t)    
    
    return answer