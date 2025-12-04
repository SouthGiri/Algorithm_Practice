import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
data.sort()
i = 0
ans = 0
while i < N-1:
    if data[i] < 0:
        if data[i+1] < 0:
            ans += data[i]*data[i+1]
            i += 2
        elif data[i+1] == 0:
            i += 2
        else:
            ans += data[i]
            i += 1
    elif data[i] == 0:
        i += 1
    else:
        if (N-i) % 2 == 1:
            ans += data[i]
            i += 1
        while i < N:
            if data[i] != 1 and data[i+1] != 1:
                ans += data[i] * data[i+1]
            else:
                ans += data[i] + data[i+1]
            i += 2

if i == N-1:
    ans += data[i]
print(ans)