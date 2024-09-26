import sys
input = sys.stdin.readline

from math import factorial

while True:
    s = input().rstrip()
    if s == '0':
        break
    ans = 0
    for i in range(len(s)):
        ans += int(s[i]) * factorial(len(s)-i)
    print(ans)