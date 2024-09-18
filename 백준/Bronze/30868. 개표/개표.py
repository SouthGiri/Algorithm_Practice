import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    for _ in range(n//5):
        print('++++', end=' ')
    for _ in range(n%5):
        print('|', end='')
    print()