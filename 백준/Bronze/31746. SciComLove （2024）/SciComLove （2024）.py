import sys
input = sys.stdin.readline

n = int(input())
s = 'SciComLove'
print(s) if n%2 == 0 else print(s[::-1])