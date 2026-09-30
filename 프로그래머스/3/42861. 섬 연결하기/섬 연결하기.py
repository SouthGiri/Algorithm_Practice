def solution(n, costs):
    # kruskal
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
            
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    parent = [i for i in range(n)]
    answer = 0
    edge = 0
    
    costs.sort(key=lambda x : x[2])
    
    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost
            edge += 1
        
        if edge == n-1:
            break
    
    return answer