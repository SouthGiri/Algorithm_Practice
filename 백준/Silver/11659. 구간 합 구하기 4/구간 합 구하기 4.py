import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.insert(0, 0)
for i in range(1, n):
    num[i+1] += num[i]

for _ in range(m):
    start, end = map(int, input().split())
    res = num[end] - num[start-1]
    
    print(res)