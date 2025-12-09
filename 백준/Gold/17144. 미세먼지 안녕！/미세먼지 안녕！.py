import sys
input = sys.stdin.readline

def diffuse():
    res = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] != 0 and room[r][c] != -1:
                cnt = 0
                amount = int(room[r][c] / 5)
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        res[nr][nc] += amount
                        cnt += 1
                res[r][c] -= amount * cnt
    
    for r in range(R):
        for c in range(C):
            room[r][c] += res[r][c]

def air():
    up, down = air_purifier
    r1, c1 = up
    r2, c2 = down
    
    r = r1 - 1
    c = c1
    room[r][c] = 0
    while r > 0:
        room[r][c] = room[r-1][c]
        r -= 1
    while c < C-1:
        room[r][c] = room[r][c+1]
        c += 1
    while r < r1:
        room[r][c] = room[r+1][c]
        r += 1
    while c > 1:
        room[r][c] = room[r][c-1]
        c -= 1
    room[r][c] = 0

    r = r2+1
    c = c2
    room[r][c] = 0
    while r < R-1:
        room[r][c] = room[r+1][c]
        r += 1
    while c < C-1:
        room[r][c] = room[r][c+1]
        c += 1
    while r > r2:
        room[r][c] = room[r-1][c]
        r -= 1
    while c > 1:
        room[r][c] = room[r][c-1]
        c -= 1
    room[r][c] = 0

def count():
    ans = 0
    for r in range(R):
        ans += sum(room[r])
    
    return ans + 2


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

R, C, T = map(int, input().split())
room = []
air_purifier = []
for r in range(R):
    li = list(map(int, input().split()))
    room.append(li)
    for c in range(C):
        if li[c] == -1:
            air_purifier.append((r, c))

for _ in range(T):
    diffuse()
    air()

print(count())