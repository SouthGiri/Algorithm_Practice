import sys
input = sys.stdin.readline
from itertools import combinations

# N 장의 카드를 받아 <=M 인 카드 3장의 합을 구해 출력
# combination sum

n, m = map(int, input().split())
li = list(map(int, input().split()))

s = 0
for i in combinations(range(len(li)), 3):
    now_s = 0
    for j in i:
        now_s += li[j]
    if now_s > s and now_s <= m:
        s = now_s

print(s)