import sys
input = sys.stdin.readline

# K = int(input())
# for _ in range(K):
#     V, E = map(int, input().split())
#     edges = []
#     for _ in range(E):
#         a, b = map(int, input().split())
#         edges.append((a, b))

#     A, B = set(), set()
    
#     for a, b in edges:
#         if a in A and b in A or a in B and b in B:
#             print('NO')
#             break
#         if a in A or b in B:
#             A.add(a)
#             B.add(b)
#         else:
#             A.add(b)
#             B.add(a)
#     else:
#         print('YES')

from collections import deque

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    group = [0] * (V+1)
    group[0] = 2
    ans = 'YES'
    q = deque()

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for start in range(1, V+1):
        if group[start]:
            continue
        
        group[start] = 1
        q.append(start)
        
        while q:
            node = q.popleft()
            
            for adj_node in graph[node]:
                if group[adj_node] == group[node]:
                    ans = 'NO'
                    break
                
                if not group[adj_node]:
                    group[adj_node] = group[node] * -1
                    q.append(adj_node)
    
    print(ans)
        