import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
ans = ''
for now in s:
    if now.isalpha():
        ans += now
    else:
        if now == '(':
            stack.append(now)
        elif now == '*' or now == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(now)
        elif now == '+' or now == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(now)
        elif now == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()

print(ans)