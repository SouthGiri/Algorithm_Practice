import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    stu, app = map(int, input().split())
    ans += (app%stu)
print(ans)