import sys
input = sys.stdin.readline

eq = input().split('-')
li = []

for i in eq:
    s = 0
    tmp = i.split('+')
    for j in tmp:
        s += int(j)
    li.append(s)

res = li[0]
for i in range(1, len(li)):
    res -= li[i]

print(res)