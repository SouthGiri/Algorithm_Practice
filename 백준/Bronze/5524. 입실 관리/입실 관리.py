import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    line = input().rstrip()
    print(line.lower())