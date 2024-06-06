import sys
input = sys.stdin.readline
import math

n = int(input())
num = list(map(int, input().split()))
t, p = map(int, input().split())

shirt = 0
for i in num:
    shirt += math.ceil(i/t)
print(shirt)

pen = n // p
one_pen = n - p*pen
print(pen, one_pen)
