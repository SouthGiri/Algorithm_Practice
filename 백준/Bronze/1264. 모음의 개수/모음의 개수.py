import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '#':
        break
    else:
        s = s.lower()
        ans = 0
        for i in ['a', 'e', 'i', 'o', 'u']:
            ans += s.count(i)
        print(ans)