import sys
input = sys.stdin.readline

n = int(input())

li = [list(map(int,input().split())) for _ in range(n)]

for i in li:
    rank = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')