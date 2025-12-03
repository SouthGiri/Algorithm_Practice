S = int(input())

res = 0
ans = 0
while res <= S:
    ans += 1
    res += ans

print(ans-1)