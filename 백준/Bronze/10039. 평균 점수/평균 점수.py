import sys
input = sys.stdin.readline

li = []
for _ in range(5):
    s = int(input())
    if s < 40:
        s = 40
    li.append(s)
print(sum(li)//5)