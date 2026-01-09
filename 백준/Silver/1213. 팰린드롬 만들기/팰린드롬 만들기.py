import sys
input = sys.stdin.readline

from collections import Counter

data = input().rstrip()

counter = Counter(data)

mid = ''
ans = ''

for key, val in counter.items():
    if val % 2 == 1:
        mid += key
        if len(mid) > 1:
            print("I'm Sorry Hansoo")
            exit()

for key, val in sorted(counter.items()):
    ans += key * (val // 2)
        
ans += mid + ans[::-1]

print(ans)