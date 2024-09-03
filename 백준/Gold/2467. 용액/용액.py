import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
left_idx, right_idx = 0, n-1

ans = abs(li[left_idx] + li[right_idx])
left = left_idx
right = right_idx

while left_idx < right_idx:
    tmp = li[left_idx] + li[right_idx]

    if abs(tmp) < ans:
        left = left_idx
        right = right_idx
        ans = abs(tmp)

        if ans == 0:
            break
    
    if tmp < 0:
        left_idx += 1
    else:
        right_idx -= 1

print(li[left], li[right])