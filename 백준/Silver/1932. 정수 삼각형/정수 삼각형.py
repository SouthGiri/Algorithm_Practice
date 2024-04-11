import sys
input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

dp = [[0]*i for i in range(1,n+1)]
dp[0] = tri[0]

# 20 = 10 21 = 10or11 22=11
# 30=20 31=20or21 32=21or22 33=22

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:
            dp[i][j] = tri[i][j] + dp[i-1][j]
        elif j == len(tri[i])-1:
            dp[i][j] = tri[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = tri[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            


print(max(dp[n-1]))