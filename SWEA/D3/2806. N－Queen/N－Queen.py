
def dfs(row):
    global ans
    if row == N:
        ans += 1
        return
    
    for col in range(N):
        if v1[col]==0 and v2[row+col]==0 and v3[row-col]==0:
            v1[col], v2[row+col], v3[row-col] = 1, 1, 1
            dfs(row+1)
            v1[col], v2[row+col], v3[row-col] = 0, 0, 0
            
            
T = int(input())
for case in range(1, T+1):
    N = int(input())
    ans = 0
    v1, v2, v3 = [[0]*(2*N) for _ in range(3)]
    dfs(0)

    print(f'#{case} {ans}')