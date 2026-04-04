from collections import deque, defaultdict

def is_diff_one(first, second):
    res = 0
    for idx in range(len(first)):
        if first[idx] != second[idx]:
            res += 1
    return True if res == 1 else False


def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = {key : False for key in words}
    
    q = deque()
    q.append((0, begin))
    
    while q:
        cost, now = q.popleft()
        for nxt in words:
            if not visited[nxt] and is_diff_one(now, nxt):
                if nxt == target:
                    answer = cost+1
                q.append((cost+1, nxt))
                visited[nxt] = True
    
    return answer