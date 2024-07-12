import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, fl1, x2, y2, fl2 = map(int, input().split())
    print(fl1 + fl2 + abs(x1-x2) + abs(y1-y2))