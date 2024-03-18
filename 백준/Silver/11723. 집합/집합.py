import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    command = list(input().split())
    proc = command[0]
    num = int(command[1]) if len(command) != 1 else None

    if proc == 'add':
        s.add(num)
    elif proc == 'remove':
        s.discard(num)
    elif proc == 'check':
        print(1) if num in s else print(0)
    elif proc == 'toggle':
        s.discard(num) if num in s else s.add(num)
    elif proc == 'all':
        s = set(range(1, 21))
    else:
        s = set()