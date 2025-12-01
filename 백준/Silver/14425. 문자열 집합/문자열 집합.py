N, M = map(int, input().split())
ans = 0
res = set()
for _ in range(N):
    res.add(input())
for _ in range(M):
    s = input()
    if s in res:
        ans += 1
print(ans)