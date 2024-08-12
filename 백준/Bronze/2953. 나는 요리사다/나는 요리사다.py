import sys
input = sys.stdin.readline

li = []
for i in range(5):
    score = list(map(int, input().split()))
    li.append(sum(score))

print(li.index(max(li))+1, max(li))