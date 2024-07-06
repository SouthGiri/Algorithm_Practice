import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if y > x:
        print('NO BRAINS')
    else:
        print('MMM BRAINS')