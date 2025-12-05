import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
ans = 0
for i in range(1, M+1):
    a, b = map(int, input().split())
    a = find(a)
    b = find(b)
    if a == b and ans == 0:
        ans = i
    union(a,b)

print(ans)