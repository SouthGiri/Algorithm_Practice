import sys
input = sys.stdin.readline

n = int(input())
price = []
for _ in range(n):
    price.append(float(input()))
price.sort()
print(price[1]) if len(str(price[1])) == 5 else print(str(price[1]) + '0')