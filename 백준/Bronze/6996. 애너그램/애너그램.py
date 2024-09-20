import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().rstrip().split()

    c = sorted(list(a))
    d = sorted(list(b))

    if c == d:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
