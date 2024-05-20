import sys
input = sys.stdin.readline

def round(x):
    if (x - int(x)) >= 0.5:
        return int(x)+1
    else:
        return int(x)

n = int(input())

if n == 0:
    print(0)

else:
    level = []
    for _ in range(n):
        level.append(int(input()))
    
    level.sort()
    elimi = round(n * 0.15)
    if elimi != 0:
        res = round(sum(level[elimi:-elimi]) / (n - 2*elimi))
    else:
        res = round(sum(level) / n)

    print(res)