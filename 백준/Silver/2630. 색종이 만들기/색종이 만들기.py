import sys
input = sys.stdin.readline

mat = []
white = blue = 0

n = int(input())
for _ in range(n):
    v = list(map(int, input().split()))
    mat.append(v)

def check(row, col, n):
    global white, blue

    cur = mat[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if cur != mat[i][j]:
                next_n = n//2
                check(row, col, next_n)
                check(row, col+next_n, next_n)
                check(row+next_n, col, next_n)
                check(row+next_n, col+next_n, next_n)
                return
            
    if cur == 0:
        white += 1
    else:
        blue += 1
    return

check(0,0,n)
print(white)
print(blue)