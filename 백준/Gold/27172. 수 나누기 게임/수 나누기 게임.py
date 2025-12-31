import sys
input = sys.stdin.readline

def eratos(x):
    for i in range(2*x, max_val+1, x):
        if i in S:
            era[i] -= 1
            era[x] += 1

N = int(input())
data = list(map(int, input().split()))
max_val = max(data)
S = set(data)

era = [0] * (max_val+1)

for x in data:
    eratos(x)

for x in data:
    print(era[x], end=' ')