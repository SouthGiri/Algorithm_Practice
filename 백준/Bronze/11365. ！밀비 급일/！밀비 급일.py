import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == 'END':
        break
    else:
        print(s[::-1])