import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().split()))

cost.sort()
time = 0

for i in range(n):
    time += ((n-i) * cost[i])

print(time)