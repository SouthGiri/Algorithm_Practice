import sys
input = sys.stdin.readline

from itertools import combinations_with_replacement as combi

n, m = map(int, input().split())

com = combi(range(1, n+1), m)
for c in com:
    print(*c)