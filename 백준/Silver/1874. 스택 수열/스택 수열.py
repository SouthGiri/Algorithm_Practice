n = int(input())

stack = []
answer = []
now = 1
possible = True

for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        now += 1
        answer.append('+')
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        possible = False
        break

if not possible:
    print('NO')
else:
    for i in answer:
        print(i)