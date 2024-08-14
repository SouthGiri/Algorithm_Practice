import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    for j in range(n-1, i, -1):
        print(' ', end='')
    print('*'*(i*2 + 1))