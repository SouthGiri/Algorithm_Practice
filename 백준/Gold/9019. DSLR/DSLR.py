import sys
input = sys.stdin.readline

from collections import deque

def opD(x, cmd):
    return (2*x) % 10000, cmd+'D'

def opS(x, cmd):
    return x-1 if x != 0 else 9999, cmd+'S'

def opL(x, cmd):
    return (x % 1000) * 10 + (x//1000), cmd+'L'

def opR(x, cmd):
    return (x%10) * 1000 + (x//10), cmd+'R'

def search(start, end):
    ch = [0 for _ in range(10001)]

    q = deque()
    q.append((start, ''))
    ch[start] = True
    
    while q:
        val, cmd = q.popleft()
        
        if val == end:
            return cmd
        
        else:
            d, dcmd = opD(val, cmd)
            s, scmd = opS(val, cmd)
            l, lcmd = opL(val, cmd)
            r, rcmd = opR(val, cmd)
            if not ch[d]:
                q.append((d, dcmd))
                ch[d] = True
            if not ch[s]:
                q.append((s, scmd))
                ch[s] = True
            if not ch[l]:
                q.append((l, lcmd))
                ch[l] = True
            if not ch[r]:
                q.append((r, rcmd))
                ch[r] = True


        
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(search(a, b))