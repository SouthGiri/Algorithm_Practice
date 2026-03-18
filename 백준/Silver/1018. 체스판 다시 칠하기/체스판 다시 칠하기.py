# W 정답과 비교해 다른 개수 계산, 64에서 빼면 B 정답과 다른 개수
# 8x8 kernel 로 잘라서 하나씩 수 계산

chess = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

N, M = map(int, input().split())

# 색칠할 최소 개수
res = N*M
mat = []

for _ in range(N):
    mat.append(list(input()))

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for r in range(8):
            for c in range(8):
                if mat[i+r][j+c] != chess[r][c]:
                    cnt += 1
        local_min = min(cnt, 64-cnt)
        res = min(local_min, res)
print(res)