import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

data.sort()

ans = [1e9, 1e9]
i, j = 0, N-1

while i < j:
    sm = data[i] + data[j]
    
    if abs(sm) < abs(sum(ans)):
        ans[0], ans[1] = data[i], data[j]

    if abs(sm) == 0: break
    
    if sm < 0:
        i += 1
    else:
        j -= 1

print(*ans)