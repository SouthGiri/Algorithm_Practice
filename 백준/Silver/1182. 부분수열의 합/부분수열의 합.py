def dfs(n, sm):
    global ans
    
    if n == N:
        return
    
    if sm+arr[n] == S:
        ans += 1

    dfs(n+1, sm)
    dfs(n+1, sm+arr[n])

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
dfs(0, 0)
print(ans)