def dfs(depth, sum_val, count):
    global ans

    if depth == max_depth:
        if count == N and sum_val == K:
	        ans += 1
        return

    # 현재 index 더하는 경우
    dfs(depth+1, sum_val+arr[depth], count+1)

    # 더하지 않는 경우
    dfs(depth+1, sum_val, count)
    
t = int(input())
max_depth = 12
arr = [i for i in range(1, max_depth+1)]
for case in range(1, t+1):
    N, K = map(int, input().split())
    ans = 0
    dfs(0, 0, 0)
    print(f'#{case} {ans}')