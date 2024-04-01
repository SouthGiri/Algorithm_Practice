import sys
input = sys.stdin.readline

m, n = map(int, input().split())

prime = [1] * (n+1)
prime[0] = prime[1] = 0

for i in range(2, int((n)**0.5)+1):
    if prime[i] == True:
        for j in range(i*2, n+1, i):
            prime[j] = False

for i in range(m, len(prime)):
    if prime[i]:
        print(i)