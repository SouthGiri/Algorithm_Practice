import sys
input = sys.stdin.readline

n = int(input())
st = input().rstrip()
ans = 0
bonus = 0

for idx in range(len(st)):
    s = st[idx]
    score = idx+1
    if s == 'O':
        ans += score
        ans += bonus
        bonus += 1
    else:
        bonus = 0

print(ans)