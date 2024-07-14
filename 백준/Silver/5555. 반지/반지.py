import sys
input = sys.stdin.readline

want = input().rstrip()
n = int(input())
ans = 0

for _ in range(n):
    line = input().rstrip()
    if want in line*2:
        ans += 1
    
print(ans)