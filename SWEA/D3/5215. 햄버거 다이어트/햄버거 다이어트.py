T = int(input())
for case in range(1, T+1):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [0] * (L+1)
    
    for score, calorie in data:
        for i in range(calorie, L+1)[::-1]:
            dp[i] = max(dp[i], dp[i-calorie] + score)

    print(f'#{case} {max(dp)}')