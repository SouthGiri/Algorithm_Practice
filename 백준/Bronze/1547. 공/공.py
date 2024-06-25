m = int(input())
ans = 1
for _ in range(m):
    a, b = map(int, input().split())
    if a == ans:
        ans = b
    elif b == ans:
        ans = a

print(ans)