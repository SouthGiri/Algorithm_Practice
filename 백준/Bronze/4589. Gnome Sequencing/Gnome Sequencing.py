n = int(input())
print('Gnomes:')
for _ in range(n):
    line = list(map(int, input().split()))
    if line == sorted(line) or line == sorted(line, reverse=True):
        print('Ordered')
    else:
        print('Unordered')