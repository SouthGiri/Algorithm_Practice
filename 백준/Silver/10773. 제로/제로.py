import sys
input = sys.stdin.readline

li = []
k = int(input())
for _ in range(k):
    x = int(input())
    if x == 0:
        li.pop()
    else:
        li.append(x)
print(sum(li))