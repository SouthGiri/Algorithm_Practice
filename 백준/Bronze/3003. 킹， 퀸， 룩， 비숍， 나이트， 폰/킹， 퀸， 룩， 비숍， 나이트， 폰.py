import sys
input = sys.stdin.readline

li = list(map(int, input().split()))
minus = [1,1,2,2,2,8]
for i in range(6):
    print(minus[i] - li[i], end=' ')