import sys
input = sys.stdin.readline

line = input().strip()
stack = []
ans = 0

for i in range(len(line)):
    if line[i] == '(':
        stack.append(line[i])
    else:
        stack.pop()
        if line[i-1] == '(':
            # stack.pop()
            ans += len(stack)
        else:
            ans += 1
            # stack.pop()

print(ans)