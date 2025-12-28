import sys
input = sys.stdin.readline

def eratos(n):
    arr = [i for i in range(n+1)]
    arr[1] = False
    for i in range(2, int(n**0.5) + 1):
        for j in range(2*i, n+1, i):
            arr[j] = False
    
    return [idx for idx in arr if idx]


N = int(input())

era = eratos(N)
start = end = 0
ans = 0

while end <= len(era):
    sm = sum(era[start:end])
    if sm == N:
        ans += 1
        end += 1
    elif sm < N:
        end += 1
    else:
        start += 1
    
print(ans)