S = list(input())

if '0' in S:
    S.sort(reverse=True)
    res = 0
    for i in S:
        res += int(i)
    if res % 3 == 0:
        print(''.join(S))
    else:
        print(-1)
else:
    print(-1)