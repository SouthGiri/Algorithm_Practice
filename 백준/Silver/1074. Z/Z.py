import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

ans = 0

while n != 0:
    n -= 1
    stand = 2**n

    # 1사분면
    if r < stand and c >= stand:
        ans += 2**(2*n) * 1
        c -= stand
    
    # 2사분면
    elif r < stand and c < stand:
        ans = ans

    # 3사분면
    elif r >= stand and c < stand:
        ans += 2**(2*n) * 2
        r -= stand
    
    # 4사분면
    else:
        ans += 2**(2*n) * 3
        c -= stand
        r -= stand

print(ans)