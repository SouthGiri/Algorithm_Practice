from math import factorial as fact

n, k = map(int, input().split())

print(int(fact(n) / fact(n-k) / fact(k)))