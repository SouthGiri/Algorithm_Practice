
def dfs(depth):
    global ans

    if depth == swap:
        ans = max(ans, int(''.join(nums)))
        return
    
    for i in range(L-1):
        for j in range(i+1, L):
            nums[i], nums[j] = nums[j], nums[i]
            if (depth, ''.join(nums)) not in visited:
                visited.append((depth, ''.join(nums)))
                dfs(depth+1)
            nums[i], nums[j] = nums[j], nums[i]

t = int(input())
for case in range(1, t+1):
    nums, swap = input().split()
    swap = int(swap)
    nums = list(nums)
    L = len(nums)
    visited = []

    ans = 0
    dfs(0)
    print(f'#{case} {ans}')