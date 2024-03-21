import sys
input = sys.stdin.readline

password = dict()
n, m = map(int, input().split())
for _ in range(n):
    li = list(input().split())
    password[li[0]] = li[1]

for _ in range(m):
    print(password[input().rstrip()])