import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    change = int(input())

    q = change // 25
    rem = change - q*25

    d = rem // 10
    rem = rem - d*10

    n = rem // 5
    rem = rem - n*5

    p = rem

    print(q, d, n, p)