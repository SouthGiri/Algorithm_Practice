import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        print(count[a])
    elif a < b:
        parent[b] = a
        count[a] += count[b]
        print(count[a])
    else:
        parent[a] = b
        count[b] += count[a]
        print(count[b])


def solve(a, b):
    if a not in parent.keys():
        parent[a] = a
        count[a] = 1
    if b not in parent.keys():
        parent[b] = b
        count[b] = 1

    union(a, b)


T = int(input())
for _ in range(T):
    parent = dict()
    count = dict()

    F = int(input())
    for _ in range(F):
        a, b = input().strip().split()
        solve(a, b)