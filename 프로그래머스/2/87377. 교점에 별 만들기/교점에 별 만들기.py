def solution(line):
    from itertools import combinations
    
    coords = set()
    
    for (a1, b1, c1), (a2, b2, c2) in combinations(line, 2):
        dom = a1*b2 - a2*b1
        
        if not dom:
            continue
        
        x = (b1*c2 - b2*c1) / dom
        y = (a2*c1 - a1*c2) / dom
        
        if x == int(x) and y == int(y):
            x, y = int(x), int(y)
            coords.add((x, y))
    

    min_x, min_y = map(min, zip(*coords))
    coords = [(x - min_x, y - min_y) for x, y in coords]
    col, row = map(max, zip(*coords))
    
    
    ans = [["."] * (col+1) for _ in range(row+1)]
    
    for x, y in coords:
        ans[row - y][x] = '*'
    
    ans = list(map(''.join, ans))
    
    return ans