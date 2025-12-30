import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()

val = int(3e9)

for i in range(N-2):
    left = i+1
    right = N-1
    
    while left < right:
        tmp = data[i] + data[left] + data[right]
        if abs(tmp) < val:
            ans = [data[i], data[left], data[right]]
            val = abs(tmp)
        
        if tmp < 0:
            left += 1
        else:
            right -= 1

print(*ans)
