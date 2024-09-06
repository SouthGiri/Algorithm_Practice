import sys
input = sys.stdin.readline


p, k = map(int, input().split())

for i in range(2, k):
    if p % i == 0:
        print('BAD {}'.format(i))
        break
else:
    print('GOOD')