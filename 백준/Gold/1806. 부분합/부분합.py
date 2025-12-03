INF = int(1e9)
N, S = map(int, input().split())
arr = list(map(int, input().split()))
i = j = 0
sum_val = 0
ans = INF

while True:
    if sum_val >= S:
        ans = min(ans, j-i)
        sum_val -= arr[i]
        i += 1
    elif j == N:
        break
    else:
        sum_val += arr[j]
        j += 1

if ans == INF:
    print(0)
else:
    print(ans)