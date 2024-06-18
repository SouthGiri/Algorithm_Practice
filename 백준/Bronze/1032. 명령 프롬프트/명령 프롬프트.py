import sys
input = sys.stdin.readline

files = []
ans = None
n = int(input())

for i in range(n):
    if i == 0:
        ans = list(input().rstrip())
    else:
        files.append(input().rstrip())


for line in files:
    for i in range(len(ans)):
        if ans[i] != line[i]:
            ans[i] = '?'

print(''.join(ans))