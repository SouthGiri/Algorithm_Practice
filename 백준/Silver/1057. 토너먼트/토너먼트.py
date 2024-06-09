import sys
input = sys.stdin.readline

n, kim, lim = map(int, input().split())

ans = 0
while kim != lim:
    kim -= kim // 2
    lim -= lim // 2
    ans += 1
print(ans)