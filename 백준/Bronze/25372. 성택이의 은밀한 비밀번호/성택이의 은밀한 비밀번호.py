n=int(input())
for _ in range(n):
    i = input().rstrip()
    if 6 <= len(i) <= 9:
        print('yes')
    else:
        print('no')