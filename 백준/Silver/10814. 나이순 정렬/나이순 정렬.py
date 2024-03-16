import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    age, name = input().split()
    li.append([i, (int(age), name)])

li.sort(key=lambda x: (x[1][0], x[0]))
for i in li:
    print(i[1][0], i[1][1])