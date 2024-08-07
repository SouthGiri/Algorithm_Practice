import sys
input = sys.stdin.readline

n = int(input())
problem = list(map(int, input().split()))
ans = []
acc = 0
for prob in problem:
    if prob == 1:
        acc += 1
        ans.append(acc)
    else:
        acc = 0
print(sum(ans))