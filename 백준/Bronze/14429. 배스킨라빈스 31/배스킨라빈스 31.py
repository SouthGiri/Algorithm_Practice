import sys
input = sys.stdin.readline

ans = []
n = int(input())
for i in range(n):
    j, m = map(int, input().split())
    r = (j-1) // (1+m)
    ans.append((i+1, (r+1) * 2))

ans.sort(key=lambda x : (x[1], x[0]))
print(ans[0][0], end=' ')
print(ans[0][1])