import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    line = input().rstrip()
    if line == 'P=NP':
        print('skipped')
        
    else:
        a, b = line.split('+')
        print(int(a) + int(b))