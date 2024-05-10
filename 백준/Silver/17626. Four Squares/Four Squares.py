import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 50001
mini = 4

for i in range(1, int(50000**0.5)):
    dp[i**2] = 1

for i in range(int(n**0.5), 0, -1):
    if dp[n]:
        mini = 1
        break
    elif dp[n - i**2]:
        mini = 2
        break
    else:
        for j in range(int((n - i**2) ** 0.5), 0, -1):
            if dp[(n - i**2) - j**2]:
                mini = 3

print(mini)