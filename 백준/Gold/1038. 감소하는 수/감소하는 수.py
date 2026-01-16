import sys
input = sys.stdin.readline

def dfs(n, num):
    if n == 10 or num[0] == '9':
        return

    for i in range(10):
        if i > int(num[0]):
            x = str(i) + num
            ans.append(int(x))
            dfs(n+1, x)

N = int(input())

ans = []

for i in range(10):
    ans.append(i)
    dfs(1, str(i))

ans.sort()
print(ans[N]) if N < len(ans) else print(-1)