c = int(input())
coke, beer = map(int, input().split())
ans = coke//2 + beer
ans = min(ans, c)
print(ans)