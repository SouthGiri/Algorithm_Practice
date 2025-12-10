import sys
input = sys.stdin.readline

S = input().strip()
pattern = input().strip()

stack = []
L = len(pattern)

for ch in S:
    stack.append(ch)
    if ''.join(stack[len(stack)-L : ]) == pattern:
        for _ in range(L):
            stack.pop()

print(''.join(stack)) if len(stack) != 0 else print('FRULA')