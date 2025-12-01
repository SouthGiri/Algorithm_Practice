from itertools import combinations

L, C = map(int, input().split())
data = list(input().split())
data.sort()
mo = set(['a', 'e', 'i', 'o', 'u'])

for cand in combinations(data, L):
    cnt = 0
    for c in cand:
        if c in mo:
            cnt += 1
    if 1 <= cnt <= L-2:
        print(''.join(cand))

