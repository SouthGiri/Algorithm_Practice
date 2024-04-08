import sys
input = sys.stdin.readline

def fpow(a, b, c):
    if b == 1:
        return a%c
    elif b % 2 == 0:
        return (fpow(a, b//2, c)**2)%c
    else:
        return ((fpow(a, b//2, c)**2)*a)%c

a,b,c = map(int, input().split())

print(fpow(a,b,c))