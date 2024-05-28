import sys
input = sys.stdin.readline

r = 31
m = 1234567891

l = int(input())
s = list(input().rstrip())

int_s = list(map(ord, s))
res = 0

for i in range(l):
    int_s[i] -= 96

for i in range(l):
    res += (int_s[i] * (r ** i))

print(res % m)