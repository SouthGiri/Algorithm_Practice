import sys
input = sys.stdin.readline

box = 0
cnt = 0

n = int(input())
for _ in range(n):
    kind, w, h, l = input().rstrip().split()
    w, h, l = int(w), int(h), int(l)

    if kind == 'A':
        box += 1000
        cnt += (w//12) * (h//12) * (l//12)

    else:
        box += 6000

box += cnt * 500
price = cnt * 4000

print(box)
print(price)