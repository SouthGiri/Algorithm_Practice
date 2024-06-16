import sys
input = sys.stdin.readline

li = []
n = int(input())
for _ in range(n):
    li.append(input().rstrip())

for i in range(n):
    print(str(i+1) + '. ' + li[i])