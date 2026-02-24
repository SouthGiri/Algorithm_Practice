import sys
input = sys.stdin.readline


def check(line):
    used = [False] * N
    for i in range(1, N):
        if abs(line[i] - line[i-1]) > 1:
            return False
        
        if line[i-1] > line[i]:
            for j in range(L):
                if i+j >= N or line[i] != line[i+j] or used[i+j]:
                    return False
                if line[i] == line[i+j]:
                    used[i+j] = True
        
        elif line[i-1] < line[i]:
            for j in range(L):
                if i-j-1 < 0 or line[i-1] != line[i-j-1] or used[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    used[i-j-1] = True
        
    return True


N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    if check([graph[i][j] for j in range(N)]):
        ans += 1

    if check([graph[j][i] for j in range(N)]):
        ans += 1

print(ans)