import sys
input = sys.stdin.readline

def construct(x):
    x += sum(map(int, str(x)))
    return x

n = int(input())

con = 0

for i in range(1, n+1):
    if n == construct(i):
        con = i
        break
print(con)