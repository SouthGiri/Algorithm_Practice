def solution(r1, r2):
    from math import floor, ceil, sqrt
    
    ans = 0
    
    for x in range(1, r2+1):
        ans += floor(sqrt(r2**2 - x**2)) + 1
        if r1 >= x:
            ans -= ceil(sqrt(r1**2 - x**2))
    
    return ans*4