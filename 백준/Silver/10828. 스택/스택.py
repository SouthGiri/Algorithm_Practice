import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = list(input().split())
    proc = command[0]

    if proc == 'push':
        stack.append(int(command[1]))
    elif proc == 'pop':
        print(stack.pop()) if len(stack) != 0 else print(-1)
    elif proc == 'size':
        print(len(stack))
    elif proc == 'empty':
        print(1) if len(stack) == 0 else print(0)
    else:
        print(stack[-1]) if len(stack) != 0 else print(-1)