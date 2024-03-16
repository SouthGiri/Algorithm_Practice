import sys
input = sys.stdin.readline

# stack 이용
# ( -> stack에 push
# ) -> stack에서 pop
# 마지막에 스택이 비어있다면 yes

t = int(input())

for _ in range(t):
    s = input().rstrip()
    stack = []
    is_vps = True
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                is_vps = False
                break
            else:
                stack.pop()
    if not stack and is_vps:
        print('YES')
    else:
        print('NO')