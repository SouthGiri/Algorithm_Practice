import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
cost = int(input())

s += cost
m += s//60
h += m//60
print(h%24, m%60, s%60)