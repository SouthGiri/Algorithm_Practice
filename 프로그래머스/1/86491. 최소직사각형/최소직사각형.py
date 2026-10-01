def solution(sizes):
    wid, hei = 0, 0
    
    for w, h in sizes:
        if w < h:
            w, h = h, w
        
        wid = max(wid, w)
        hei = max(hei, h)
    
    answer = wid * hei
    
    return answer