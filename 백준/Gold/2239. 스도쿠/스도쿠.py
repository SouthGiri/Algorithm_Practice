import sys
input = sys.stdin.readline

def row(r, num):
    for x in range(9):
        if num == A[r][x]:
            return False
    return True

def col(c, num):
    for x in range(9):
        if num == A[x][c]:
            return False
    return True

def box(r, c, num):
    nr = (r//3) * 3
    nc = (c//3) * 3
    for x in range(3):
        for y in range(3):
            if A[nr+x][nc+y] == num:
                return False
    return True

def dfs(n):
    if n >= len(zeros):
        for i in range(9):
            print(''.join(map(str, A[i])))
        exit()
    nr, nc = zeros[n]
    for num in range(1, 10):
        if row(nr, num) and col(nc, num) and box(nr, nc, num):
            A[nr][nc] = num
            dfs(n+1)
            A[nr][nc] = 0
                

A = []
zeros = []
for i in range(9):
    data = list(map(int, input().strip()))
    for j in range(9):
        if data[j] == 0:
            zeros.append((i, j))
    A.append(data)

dfs(0)