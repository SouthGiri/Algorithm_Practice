# 출발점이 속한 시스템 1과 도착점이 속한 시스템 3,4 -> set 개수

def in_system(x, y, cx, cy, r):
    dist = (abs(x-cx)**2 + abs(y-cy)**2) ** 0.5
    if dist < r:
        return True
    else:
        return False

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    src, dst = set(), set()
    for i in range(n):
        cx, cy, r = map(int, input().split())
        if in_system(x1, y1, cx, cy, r):
            src.add(i)
        if in_system(x2, y2, cx, cy, r):
            dst.add(i)
    uni = src.union(dst)
    dup = src.intersection(dst)
    print(len(uni) - len(dup))