N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = 0
min_cost = cost[0]

for i in range(N-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    
    ans += (min_cost * dist[i])

print(ans)