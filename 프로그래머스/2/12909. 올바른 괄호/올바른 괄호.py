def solution(s):
    answer = True
    
    stack = []
    for _s in s:
        if _s == '(':
            stack.append(_s)
        elif stack:
            stack.pop()
        else:
            return False
    
    if stack:
        return False

    return True