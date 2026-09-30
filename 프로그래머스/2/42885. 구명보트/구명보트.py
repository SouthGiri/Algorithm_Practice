def solution(people, limit):
    N = len(people)
    pair = 0
    
    people.sort()
    
    a, b = 0, N-1
    
    while a < b:
        if people[a] + people[b] <= limit:
            a += 1
            pair += 1
        b -= 1
    
    return N - pair