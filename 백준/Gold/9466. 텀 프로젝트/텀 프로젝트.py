import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(start):
    global ans

    visited[start] = True
    dst = graph[start]
    cycle.append(dst)
    
    if visited[dst]:
        ans -= len(cycle[cycle.index(dst):])-1
        return
    else:
        dfs(dst)


T = int(input())
for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    ans = N

    for student in range(1, N+1):
        if not visited[student]:
            cycle = [student]
            dfs(student)

    print(ans)