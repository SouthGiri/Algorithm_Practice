
T = int(input())
for _ in range(T):
    src, dst = map(int, input().split())
    diff = dst-src
    rep = 0
    while diff > rep*(rep+1):
        rep += 1
    
    if diff <= rep**2:
        ans = 2*rep - 1
    else:
        ans = 2*rep
    
    print(ans)