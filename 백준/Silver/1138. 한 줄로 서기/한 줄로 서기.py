import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

ans = [0] * N
cand = list(range(N))

for idx, x in enumerate(data):
    ans[cand.pop(x)] = idx+1

print(*ans)