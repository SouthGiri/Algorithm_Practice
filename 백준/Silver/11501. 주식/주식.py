import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))

    now = N - 1
    pre = now - 1

    ans = 0

    while now > 0:
        while pre >= 0 and days[pre] < days[now]:
            ans = ans - days[pre] + days[now]
            pre -= 1
        
        now = pre
        pre = now - 1

    print(ans)