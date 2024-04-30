import sys
input = sys.stdin.readline

from itertools import combinations

def dist(a, b):
    dist = 0
    for i, j in zip(a, b):
        if i != j:
            dist += 1
    return dist

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().rstrip().split()

    if n > 32:
        print(0)
    else:
        res = 13
        li = combinations(mbti, 3)
        for a, b, c in li:
            distance = 0
            distance += dist(a, b)
            distance += dist(a, c)
            distance += dist(b, c)
            res = min(distance, res)

        print(res)
