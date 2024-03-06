import sys
N = int(input())

group = 0

for _ in range(N):
    word = sys.stdin.readline()
    li = []
    is_group = True
    for i in word:
        if i not in li:
            li.append(i)
        else:
            if i != li[len(li) - 1]:
                is_group = False
                break
    if is_group:
        group += 1

print(group)