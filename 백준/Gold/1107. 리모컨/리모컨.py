import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m :
    broken = list(input().split())
else:
    broken = []

ans = abs(100 - n)

for num in range(1_000_001):
    for N in str(num):
        if N in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num-n))

print(ans)