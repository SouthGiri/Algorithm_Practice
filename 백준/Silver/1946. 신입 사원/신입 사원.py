import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort()
    ans = 1
    last = data[0]

    for now in data[1:]:
        if now[0] < last[0] or now[1] < last[1]:
            ans += 1
            last = now

    print(ans)