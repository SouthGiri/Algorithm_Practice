def solution(k, d):
    answer = 0
    y = d
    for x in range(0, d+1, k):
        while y >= 0:
            if (x**2 + y**2)**0.5 <= d:
                answer += (y//k)+1
                break
            y -= 1
            
    return answer