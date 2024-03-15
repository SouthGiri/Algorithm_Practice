import sys
input = sys.stdin.readline

n = int(input())
res = []
for _ in range(n):
    res.append(tuple(map(int, input().split())))

#res.sort(key=lambda x : (x[0], x[1]))
res.sort()

for i in res:
    print(i[0], i[1])