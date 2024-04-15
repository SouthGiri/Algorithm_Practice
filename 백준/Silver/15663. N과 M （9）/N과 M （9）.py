import sys
input = sys.stdin.readline

from itertools import permutations

n, m = map(int, input().split())
li = list(map(int, input().split()))

per = list(set(permutations(li, m)))
per.sort()

for i in per:
    for j in i:
        print(j, end=' ')
    print()