import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

ans = [-1] * N
stack = []

for i in range(N):
    while stack and data[stack[-1]] < data[i]:
        ans[stack.pop()] = data[i]
    stack.append(i)

print(*ans)