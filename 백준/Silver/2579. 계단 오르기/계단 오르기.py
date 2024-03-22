import sys
input = sys.stdin.readline

# 1. 한 번에 하나 or 둘
# 2. 연속된 3개 계단 x
# 3. 마지막 계단 반드시 밟
# DP
# 마지막-1 , 마지막-2 둘 중 하나만 밟

h = int(input())
stair = [0] + [int(input()) for i in range(1, h + 1)]
if h < 2: # 주어진 계단의 수가 2보다 작을 경우 위와 같이 stair 배열을 할당할 경우 예외처리를 해주지 않으면 index error가 발생한다
	print(stair[h])
else:
	dp = [0] * (h + 1)
	dp[1] = stair[1]
	dp[2] = dp[1] + stair[2]
	for i in range(3, h + 1):
		dp[i] = max(dp[i - 2], dp[i - 3] + stair[i - 1]) + stair[i]
	print(dp[h])