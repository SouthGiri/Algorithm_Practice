import sys
input = sys.stdin.readline

from collections import deque

line = input().strip()
ans = ''
q = deque()
for ch in line:
    if ch == '<':
        while q:
            ans += q.pop()
        q.append(ch)
    elif ch == '>':
        while q:
            ans += q.popleft()
        ans += ch
    elif ch == ' ':
        if q[0] == '<':
            q.append(ch)
        else:
            while q:
                ans += q.pop()
            ans += ' '
    else:
        q.append(ch)

while q:
    ans += q.pop()
print(ans)