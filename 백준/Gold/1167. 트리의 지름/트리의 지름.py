import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    node = list(map(int, input().split()))[:-1]
    for i in range(1, len(node)//2 + 1):
        graph[node[0]].append([node[i*2 - 1], node[i*2]])

def dfs(start, cost):
    for adj_node, dist in graph[start]:
        acc_dist = dist + cost
        if visited[adj_node] == -1:
            visited[adj_node] = acc_dist
            dfs(adj_node, acc_dist)

visited = [-1 for _ in range(v+1)]
visited[1] = 0
dfs(1, 0)

start_node = visited.index(max(visited))
visited = [-1 for _ in range(v+1)]
visited[start_node] = 0
dfs(start_node, 0)

print(max(visited))