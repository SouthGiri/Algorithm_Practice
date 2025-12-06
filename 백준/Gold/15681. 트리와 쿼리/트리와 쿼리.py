import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def make_tree(current, parent):
    for adj_node in graph[current]:
        if adj_node != parent:
            children[current].append(adj_node)
            make_tree(adj_node, current)

def count_subtree(current):
    ans[current] = 1
    for child in children[current]:
        count_subtree(child)
        ans[current] += ans[child]

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
children = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

make_tree(R, 0)

ans = [0] * (N+1)
count_subtree(R)

for _ in range(Q):
    q = int(input())
    print(ans[q])