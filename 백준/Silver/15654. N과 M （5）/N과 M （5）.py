import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

from itertools import permutations

res = list(permutations(li, m))

for i in res:
    print(*i)