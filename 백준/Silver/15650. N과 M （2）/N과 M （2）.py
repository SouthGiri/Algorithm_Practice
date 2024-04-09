import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())

li = list(combinations(range(1, n+1), m))

for i in li:
    for j in i:
        print(j, end=' ')
    print()