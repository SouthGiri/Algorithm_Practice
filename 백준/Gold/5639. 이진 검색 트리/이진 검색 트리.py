import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

def solve(arr):
    if len(arr) == 0:
        return
    
    left, right = [], []
    mid = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > mid:
            left = arr[1:i]
            right = arr[i:]
            break
    else:
        left = arr[1:]

    solve(left)
    solve(right)
    print(mid)

solve(arr)