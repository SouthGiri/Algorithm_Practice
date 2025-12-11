import sys
input = sys.stdin.readline

N = int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N)]
dp[0] = costs[0]

INF = 1e9
ans = INF

for start in range(3):
    avail = [0,1,2]
    avail.remove(start)
    dp[1][start] = INF
    for one in avail:
        dp[1][one] = dp[0][start] + costs[1][one]

    for home in range(2, N):
        dp[home][0] = min(dp[home-1][1], dp[home-1][2]) + costs[home][0]
        dp[home][1] = min(dp[home-1][0], dp[home-1][2]) + costs[home][1]
        dp[home][2] = min(dp[home-1][1], dp[home-1][0]) + costs[home][2]
    
    for av in avail:
        ans = min(ans, dp[N-1][av])

print(ans)