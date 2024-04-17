import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dic = dict()
    for _ in range(n):
        name, kind = input().split()
        if kind in dic.keys():
            dic[kind] += 1
        else:
            dic[kind] = 2

    res = 1
    for i in dic.keys():
        res *= dic[i]
    
    print(res-1)