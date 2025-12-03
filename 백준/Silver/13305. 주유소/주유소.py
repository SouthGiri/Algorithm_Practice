N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = 0
cost = cost[:-1]
while len(cost) > 0:
    stop = cost.index(min(cost))
    ans += cost[stop] * sum(dist[stop:])
    cost = cost[:stop]
    dist = dist[:stop]

print(ans)