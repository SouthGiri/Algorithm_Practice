INF = int(1e9)
N, S = map(int, input().split())
arr = list(map(int, input().split()))
i = j = 0
sum_val = arr[0]
ans = INF

while i < N and j < N:
    if i > j:
        j = i
    while sum_val < S and j < N-1:
        j += 1
        sum_val += arr[j]
        
    if sum_val >= S:
        ans = min(ans, j-i+1)
    
    sum_val -= arr[i]
    i += 1

if ans == INF:
    print(0)
else:
    print(ans)