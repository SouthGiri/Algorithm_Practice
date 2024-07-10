import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

def dfs(node, cost):
    for adj_node, weight in tree[node]:
        acc_weight = cost + weight
        if visited[adj_node] == -1:
            visited[adj_node] = acc_weight
            dfs(adj_node, acc_weight)


visited = [-1]*(n+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1]*(n+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))